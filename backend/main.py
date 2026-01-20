"""
Prompt Refinement Tool - Backend API
This module implements a two-step AI pipeline for improving user prompts.
Supports Google Gemini API (FREE) or OpenAI API
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from typing import Optional
import json

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Prompt Refinement API",
    description="Automatically transforms vague prompts into structured, optimized prompts",
    version="1.0.0"
)

# Configure CORS
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Determine which API to use
API_PROVIDER = os.getenv("API_PROVIDER", "gemini").lower()  # "gemini" or "openai"

if API_PROVIDER == "gemini":
    from google import genai
    from google.genai import types
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if GEMINI_API_KEY:
        gemini_client = genai.Client(api_key=GEMINI_API_KEY)
        MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    else:
        gemini_client = None
else:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")


# Request/Response Models
class PromptRequest(BaseModel):
    raw_prompt: str


class PromptAnalysis(BaseModel):
    intent: str
    domain: str
    role: str
    missing_details: list[str]
    output_format: str


class PromptResponse(BaseModel):
    refined_prompt: str
    analysis: PromptAnalysis
    improvements: str


# Helper function to call LLM
def call_llm(system_prompt: str, user_prompt: str, use_json: bool = False) -> str:
    """Call the configured LLM (Gemini or OpenAI)"""
    try:
        if API_PROVIDER == "gemini":
            if not gemini_client:
                raise Exception("Gemini API key not configured")
            
            full_prompt = f"{system_prompt}\n\nUser request: {user_prompt}"
            if use_json:
                full_prompt += "\n\nRespond ONLY with valid JSON. No markdown, no explanation."
            
            response = gemini_client.models.generate_content(
                model=MODEL_NAME,
                contents=full_prompt
            )
            return response.text
        else:
            # OpenAI
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            
            kwargs = {"model": MODEL_NAME, "messages": messages, "temperature": 0.5}
            if use_json:
                kwargs["response_format"] = {"type": "json_object"}
            
            response = client.chat.completions.create(**kwargs)
            return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM API Error: {str(e)}")


# Step 1: Analyze the raw prompt
def analyze_prompt(raw_prompt: str) -> PromptAnalysis:
    """
    Analyzes the raw prompt to extract intent, domain, role, and missing details.
    This is the first step of the two-step AI pipeline.
    """
    
    analysis_system_prompt = """You are an expert prompt engineer. Your task is to analyze a raw user prompt and extract key information.

Analyze the following aspects:
1. Intent: What is the user trying to accomplish? (e.g., code generation, explanation, content creation, analysis)
2. Domain: What field or area does this relate to? (e.g., web development, data science, education, marketing)
3. Role: What professional role would best fulfill this request? (e.g., software engineer, teacher, data analyst)
4. Missing Details: What important constraints, specifications, or context is missing?
5. Output Format: What format would be most appropriate for the final output?

Respond in JSON format with these exact keys: intent, domain, role, missing_details (array), output_format"""

    try:
        response_text = call_llm(
            analysis_system_prompt,
            f"Analyze this prompt: {raw_prompt}",
            use_json=True
        )
        
        # Clean response if it has markdown code blocks
        response_text = response_text.strip()
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
            response_text = response_text.strip()
        
        analysis_data = json.loads(response_text)
        
        return PromptAnalysis(
            intent=analysis_data.get("intent", "Unknown"),
            domain=analysis_data.get("domain", "General"),
            role=analysis_data.get("role", "Expert"),
            missing_details=analysis_data.get("missing_details", []),
            output_format=analysis_data.get("output_format", "Structured text")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing prompt: {str(e)}")


# Step 2: Generate refined prompt
def refine_prompt(raw_prompt: str, analysis: PromptAnalysis) -> tuple[str, str]:
    """
    Generates an optimized, structured prompt based on the analysis.
    This is the second step of the two-step AI pipeline.
    Returns: (refined_prompt, improvements_explanation)
    """
    
    refinement_system_prompt = f"""You are an expert prompt engineer. Your task is to transform a raw prompt into a clear, structured, high-quality prompt optimized for LLMs.

Use this analysis:
- Intent: {analysis.intent}
- Domain: {analysis.domain}
- Role: {analysis.role}
- Missing details to add: {', '.join(analysis.missing_details)}
- Desired output format: {analysis.output_format}

Create an improved prompt following this EXACT structure:

Act as a [role].

Task:
[Clear, specific task description]

Requirements:
- [Specific constraint 1]
- [Specific constraint 2]
- [Specific constraint 3]
- [Additional constraints as needed]

Output:
- [Expected output format]
- [Additional output specifications]

Make the prompt clear, specific, and actionable. Add relevant constraints and details that will help an LLM produce better results.

IMPORTANT: Only return the improved prompt itself, nothing else. Do not add any preamble or explanation."""

    improvements_system_prompt = """You are a prompt engineering teacher. Briefly explain (in 2-3 sentences) what improvements were made to transform the raw prompt into the refined version. Focus on the key enhancements."""

    try:
        # Generate refined prompt
        refined_prompt = call_llm(
            refinement_system_prompt,
            f"Improve this prompt: {raw_prompt}",
            use_json=False
        )
        
        # Generate explanation of improvements
        improvements = call_llm(
            improvements_system_prompt,
            f"Original: {raw_prompt}\n\nRefined: {refined_prompt}\n\nWhat improvements were made?",
            use_json=False
        )
        
        return refined_prompt.strip(), improvements.strip()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error refining prompt: {str(e)}")


# API Endpoints
@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "Prompt Refinement API",
        "version": "1.0.0"
    }


@app.post("/api/refine", response_model=PromptResponse)
async def refine_user_prompt(request: PromptRequest):
    """
    Main endpoint: Takes a raw prompt and returns a refined, structured version.
    Implements the two-step AI pipeline (analyze + refine).
    """
    
    if not request.raw_prompt or len(request.raw_prompt.strip()) < 5:
        raise HTTPException(status_code=400, detail="Prompt must be at least 5 characters long")
    
    try:
        # Step 1: Analyze the prompt
        analysis = analyze_prompt(request.raw_prompt)
        
        # Step 2: Generate refined prompt
        refined_prompt, improvements = refine_prompt(request.raw_prompt, analysis)
        
        return PromptResponse(
            refined_prompt=refined_prompt,
            analysis=analysis,
            improvements=improvements
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.get("/api/health")
async def health_check():
    """Health check endpoint for monitoring"""
    api_key_set = bool(os.getenv("GEMINI_API_KEY") if API_PROVIDER == "gemini" else os.getenv("OPENAI_API_KEY"))
    return {
        "status": "healthy",
        "api_provider": API_PROVIDER,
        "api_key_configured": api_key_set,
        "model": MODEL_NAME
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
