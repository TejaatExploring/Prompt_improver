# 🚀 Prompt Refinement Tool

An intelligent web-based Generative AI application that automatically transforms vague user prompts into clear, structured, high-quality prompts optimized for Large Language Models (LLMs) like ChatGPT or Claude.

![Prompt Refinement Tool](https://img.shields.io/badge/AI-Prompt_Engineering-blueviolet)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![React](https://img.shields.io/badge/React-18.2-61dafb)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Examples](#examples)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This tool solves a common problem: **most users write vague prompts** that lack structure, constraints, and context, leading to poor AI outputs. Instead of requiring users to learn prompt engineering, this application **automatically applies prompt engineering principles** behind the scenes.

### 🆓 FREE Option Available!
**This project now supports Google Gemini API (completely FREE)** with generous limits - no credit card required!

### What It Does:
- ✅ Accepts a single raw prompt from the user
- ✅ Automatically detects intent, domain, role, and missing details
- ✅ Generates a structured, optimized prompt ready for LLMs
- ✅ Provides analysis and improvement explanations

### What It Does NOT Do:
- ❌ Act as a chatbot
- ❌ Generate final answers to user tasks
- ❌ Require manual configuration or dropdown selections

---

## ✨ Features

### 🔍 Two-Step AI Pipeline

1. **Prompt Analysis** (Internal)
   - Detects user intent (code generation, explanation, etc.)
   - Identifies domain (web development, data science, etc.)
   - Determines appropriate professional role
   - Finds missing constraints and details

2. **Prompt Refinement** (Output)
   - Generates structured prompt with clear task description
   - Adds specific requirements and constraints
   - Defines expected output format
   - Provides improvement explanation

### 🎨 User Interface
- Single text input for raw prompts
- Clean, modern, responsive design
- Real-time prompt refinement
- Copy-to-clipboard functionality
- Automatic analysis display
- Mobile-friendly interface

---

## 🛠 Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **OpenAI API** - LLM integration (GPT-4 or GPT-3.5)
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **Vite** - Build tool
- **Axios** - HTTP client
- **CSS3** - Modern styling with gradients and animations

---

## 📁 Project Structure

```
Prompt_improver/
├── backend/
│   ├── main.py                 # FastAPI application with AI pipeline
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example           # Environment variables template
│   └── .env                   # Your API keys (create this)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main React component
│   │   ├── App.css            # Component styles
│   │   ├── main.jsx           # React entry point
│   │   └── index.css          # Global styles
│   ├── index.html             # HTML template
│   ├── vite.config.js         # Vite configuration
│   ├── package.json           # Node dependencies
│   ├── .env.example           # Frontend env template
│   └── .env                   # Frontend config (create this)
│
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.9+** installed
- **Node.js 16+** and npm installed
- **FREE Google Gemini API Key** ([Get one here](https://aistudio.google.com/app/apikey)) 
  - OR OpenAI API Key (paid, [Get one here](https://platform.openai.com/api-keys))

### Step 1: Clone the Repository
```bash
cd c:\Users\bhanu\OneDrive\Desktop\GenAI_Prj\Prompt_improver
```

### Step 2: Backend Setup

#### 2.1 Create Python Virtual Environment
```bash
cd backend
python -m venv venv
```

#### 2.2 Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

#### 2.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 2.4 Configure Environment Variables
```bash
# Copy the example file
copy .env.example .env
```

**Edit `backend\.env`:**

**Option 1: FREE Google Gemini (Recommended)**
```env
API_PROVIDER=gemini
GEMINI_API_KEY=AIza...your-free-gemini-key-here
MODEL_NAME=gemini-1.5-flash
CORS_ORIGINS=http://localhost:3000
```

**Option 2: OpenAI (Paid)**
```env
API_PROVIDER=openai
OPENAI_API_KEY=sk-your-openai-key-here
MODEL_NAME=gpt-4o-mini
CORS_ORIGINS=http://localhost:3000
```

**Get FREE Gemini API Key**: Visit https://aistudio.google.com/app/apikey (No credit card required!)

### Step 3: Frontend Setup

#### 3.1 Navigate to Frontend Directory
```bash
cd ..\frontend
```

#### 3.2 Install Node Dependencies
```bash
npm install
```

#### 3.3 Configure Frontend Environment
```bash
# Copy the example file
copy .env.example .env
```

**Edit `frontend\.env`:**
```env
VITE_API_URL=http://localhost:8000
```

---

## 🎮 Usage

### Starting the Application

You need to run both backend and frontend servers.

#### Terminal 1: Start Backend Server
```bash
cd backend
venv\Scripts\activate    # Activate virtual environment
python main.py
```

Backend will run at: **http://localhost:8000**

#### Terminal 2: Start Frontend Server
```bash
cd frontend
npm run dev
```

Frontend will run at: **http://localhost:3000**

### Using the Tool

1. **Open your browser** to `http://localhost:3000`
2. **Enter a raw prompt** in the text box (e.g., "Write code for login page")
3. **Click "Refine Prompt"**
4. **View the results:**
   - Structured, optimized prompt
   - Automatic analysis (intent, domain, role)
   - Explanation of improvements
5. **Copy the refined prompt** to use with any LLM

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### `GET /`
Health check endpoint

**Response:**
```json
{
  "status": "online",
  "service": "Prompt Refinement API",
  "version": "1.0.0"
}
```

#### `POST /api/refine`
Main endpoint for prompt refinement

**Request:**
```json
{
  "raw_prompt": "Write code for login page"
}
```

**Response:**
```json
{
  "refined_prompt": "Act as a frontend web developer.\n\nTask:\nCreate a login page...",
  "analysis": {
    "intent": "Code generation",
    "domain": "Web development",
    "role": "Frontend developer",
    "missing_details": ["validation", "responsiveness"],
    "output_format": "Complete HTML/CSS/JS code"
  },
  "improvements": "The refined prompt adds specific requirements..."
}
```

#### `GET /api/health`
Detailed health check

**Response:**
```json
{
  "status": "healthy",
  "api_key_configured": true,
  "model": "gpt-4o-mini"
}
```

---

## 💡 Examples

### Example 1: Code Generation

**Input:**
```
Write code for login page
```

**Output:**
```
Act as a frontend web developer.

Task:
Create a login page for a web application.

Requirements:
- Include email and password input fields
- Implement client-side validation
- Ensure responsive design
- Follow basic accessibility practices

Output:
- Provide complete HTML, CSS, and JavaScript code
- Include a brief explanation of the logic
```

### Example 2: Educational Content

**Input:**
```
Explain sorting
```

**Output:**
```
Act as a computer science teacher.

Task:
Explain sorting algorithms in a clear and structured manner.

Requirements:
- Define what sorting is and why it's important
- Cover at least 3 common sorting algorithms (Bubble Sort, Quick Sort, Merge Sort)
- Include time and space complexity for each
- Provide simple examples to illustrate concepts

Output:
- A structured explanation with clear sections
- Simple code examples or pseudocode
- Visual descriptions of how each algorithm works
```

### Example 3: Content Creation

**Input:**
```
Summarize this
```

**Output:**
```
Act as a professional content summarizer.

Task:
Create a comprehensive summary of the provided content.

Requirements:
- Identify and extract main ideas and key points
- Maintain the original context and meaning
- Keep the summary concise (20-30% of original length)
- Use clear, professional language

Output:
- A well-structured summary with bullet points or paragraphs
- Highlight critical information and conclusions
```

---

## ⚙️ Configuration

### Backend Configuration (`backend/.env`)

```env
# OpenAI API Key (REQUIRED)
OPENAI_API_KEY=sk-your-key-here

# Model Selection
# Options: gpt-4o-mini, gpt-4o, gpt-4, gpt-3.5-turbo
MODEL_NAME=gpt-4o-mini

# CORS Settings
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Frontend Configuration (`frontend/.env`)

```env
# Backend API URL
VITE_API_URL=http://localhost:8000
```

### Changing the AI Model

To use a different OpenAI model, edit `backend/.env`:

```env
# For more powerful responses (higher cost)
MODEL_NAME=gpt-4o

# For faster, cheaper responses
MODEL_NAME=gpt-4o-mini
```

---

## 🔧 Troubleshooting

### Issue: "Module not found" errors

**Solution:**
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### Issue: "API key not configured"

**Solution:**
- Ensure you created `backend/.env` from `backend/.env.example`
- Add your actual OpenAI API key
- Restart the backend server

### Issue: CORS errors in browser

**Solution:**
- Check that `CORS_ORIGINS` in `backend/.env` includes your frontend URL
- Restart the backend server after changes

### Issue: Frontend can't connect to backend

**Solution:**
- Verify backend is running on port 8000
- Check `VITE_API_URL` in `frontend/.env` is correct
- Ensure no firewall blocking localhost connections

### Issue: "Rate limit exceeded" from OpenAI

**Solution:**
- You've hit OpenAI API rate limits
- Wait a few minutes or upgrade your API plan
- Consider using `gpt-4o-mini` for lower costs

---

## 📦 Production Deployment

### Backend Deployment
- Use a production ASGI server (Gunicorn + Uvicorn)
- Set up proper environment variables
- Enable HTTPS
- Configure proper CORS origins

### Frontend Deployment
```bash
cd frontend
npm run build
# Deploy the 'dist' folder to your hosting service
```

---

## 🎯 Success Criteria

This project successfully meets all requirements:

✅ **Single Input** - User enters only a raw prompt  
✅ **Automatic Detection** - System detects intent, domain, role automatically  
✅ **No Manual Config** - No dropdowns or manual selections required  
✅ **Structured Output** - Generates clear, reusable prompts  
✅ **Two-Step Pipeline** - Analysis + Refinement process  
✅ **Clean UI** - Single text box + output display  
✅ **Improvement Tool** - Refines prompts, doesn't answer them  

---

## 📝 License

This project is created for educational purposes.

---

## 🤝 Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Verify your OpenAI API key is valid and has credits
3. Ensure all dependencies are installed correctly

---

## 🌟 Features Roadmap

- [ ] Support for multiple LLM providers (Anthropic Claude, Google Gemini)
- [ ] Prompt history and favorites
- [ ] Batch prompt refinement
- [ ] Export refined prompts to various formats
- [ ] User accounts and saved templates

---

**Built with ❤️ for better AI interactions**
