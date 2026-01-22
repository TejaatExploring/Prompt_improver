# 🎨 Visual Architecture: Detail Levels

## Before vs After

### ❌ BEFORE (Single Output)
```
User Input
    ↓
[Analyze Prompt]
    ↓
[Generate DETAILED Prompt]  ← Only one option!
    ↓
Overwhelming Output
```

**Problem:** Everyone got the same detailed output, regardless of:
- Their experience level
- The complexity of their task
- Which model they're using
- How much detail they actually need

---

### ✅ AFTER (Three Options)

```
User Input
    ↓
[Analyze Prompt]
    ↓
[User Selects Detail Level] ← NEW!
    ↓
    ├─→ Simple: Quick & Concise
    ├─→ Moderate: Balanced ⭐ (default)
    └─→ Detailed: Comprehensive
    ↓
Appropriate Output
```

**Solution:** Users choose the right level for their needs!

---

## System Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Text Input: "Write code for login page"           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Detail Level Selector (NEW!)                       │   │
│  │  ○ Simple     ● Moderate ⭐    ○ Detailed          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌────────────────────────────────┐                        │
│  │   [Refine Prompt] Button       │                        │
│  └────────────────────────────────┘                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
                    API Request
                 (with detail_level)
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      BACKEND PIPELINE                        │
│                                                              │
│  Step 1: Analyze Prompt                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Detect intent                                     │   │
│  │ • Identify domain                                   │   │
│  │ • Determine role                                    │   │
│  │ • Find missing details                              │   │
│  └─────────────────────────────────────────────────────┘   │
│                            ↓                                 │
│  Step 2: Generate Refined Prompt (Based on Level)           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ IF detail_level == "simple":                        │   │
│  │   → Generate 2-4 sentence concise prompt           │   │
│  │                                                      │   │
│  │ ELIF detail_level == "moderate":                    │   │
│  │   → Generate structured prompt with 4-5 points     │   │
│  │                                                      │   │
│  │ ELIF detail_level == "detailed":                    │   │
│  │   → Generate comprehensive enterprise prompt       │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
                    API Response
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                       OUTPUT DISPLAY                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Refined Prompt                            [Copy]   │   │
│  │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │   │
│  │  [Generated prompt appears here]                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Analysis: Intent, Domain, Role, Output Format      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Improvements: What was changed and why              │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Changes

### Frontend (App.jsx)
```jsx
// NEW STATE
const [detailLevel, setDetailLevel] = useState('moderate');

// NEW UI COMPONENT
<div className="detail-level-selector">
  <label>Detail Level:</label>
  <div className="radio-group">
    <label className="radio-option">
      <input type="radio" value="simple" 
             checked={detailLevel === 'simple'}
             onChange={(e) => setDetailLevel(e.target.value)} />
      <span>Simple</span>
      <span className="radio-description">Quick & concise</span>
    </label>
    {/* ... moderate and detailed options ... */}
  </div>
</div>

// UPDATED API CALL
const response = await axios.post(`${API_URL}/api/refine`, {
  raw_prompt: rawPrompt,
  detail_level: detailLevel  // NEW!
});
```

### Backend (main.py)
```python
# UPDATED REQUEST MODEL
class PromptRequest(BaseModel):
    raw_prompt: str
    detail_level: Optional[str] = "moderate"  # NEW!

# UPDATED FUNCTION SIGNATURE
def refine_prompt(
    raw_prompt: str, 
    analysis: PromptAnalysis, 
    detail_level: str = "moderate"  # NEW!
) -> tuple[str, str]:
    
    # NEW LOGIC
    if detail_level == "simple":
        # Generate concise prompt
    elif detail_level == "moderate":
        # Generate balanced prompt
    else:  # detailed
        # Generate comprehensive prompt
```

---

## Data Flow

```
┌─────────────┐
│ User Types  │
│   Prompt    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Selects     │
│ Level       │ ← NEW STEP!
└──────┬──────┘
       │
       ▼
┌─────────────────────────────┐
│ Frontend Sends:             │
│ {                           │
│   raw_prompt: "...",        │
│   detail_level: "moderate"  │
│ }                           │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ Backend Analyzes            │
│ (Same as before)            │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ Backend Generates           │
│ Based on Level ← NEW!       │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ Frontend Displays           │
│ Appropriate Output          │
└─────────────────────────────┘
```

---

## Code Execution Path

### Example: User selects "Moderate"

```
1. User enters: "Write code for login page"
2. User selects: ● Moderate
3. User clicks: [Refine Prompt]

   ↓ Frontend sends

4. POST /api/refine
   Body: { 
     raw_prompt: "Write code for login page",
     detail_level: "moderate"
   }

   ↓ Backend receives

5. analyze_prompt()
   Returns: {
     intent: "Code generation",
     domain: "Web development",
     role: "Front-end Developer",
     missing_details: [...],
     output_format: "React code"
   }

   ↓ Backend generates

6. refine_prompt(raw_prompt, analysis, "moderate")
   
   ↓ Checks level
   
7. if detail_level == "moderate":
     Use moderate template
     → Generate structured prompt with 4-5 points
     
   ↓ Returns

8. Response: {
     refined_prompt: "Act as a Front-end Developer...",
     analysis: {...},
     improvements: "...",
     detail_level: "moderate"
   }

   ↓ Frontend displays

9. Shows structured output (not overwhelming!)
```

---

## Key Architecture Points

### 1. **Separation of Concerns**
- Analysis step (unchanged)
- Generation step (now configurable)
- Presentation (shows appropriate detail)

### 2. **Extensibility**
Want to add a 4th level? Just add:
- New radio button in frontend
- New condition in backend
- New template in `refine_prompt()`

### 3. **Backward Compatibility**
Old API calls without `detail_level` still work:
- Defaults to "moderate" (better than old "detailed"!)
- No breaking changes

### 4. **User Control**
- Frontend provides clear UI
- Backend respects user choice
- Default is sensible (moderate)

---

## Visual Output Comparison

```
SIMPLE (40 words)
┌─────────────────────────────────────┐
│ Act as a Developer. Create login   │
│ page with React and CSS. Include   │
│ email/password fields, validation,  │
│ and submit button.                  │
└─────────────────────────────────────┘

MODERATE (65 words) ⭐
┌─────────────────────────────────────┐
│ Act as a Developer.                 │
│                                     │
│ Task: Create login page for React. │
│                                     │
│ Requirements:                       │
│ - React functional components       │
│ - Email/password validation         │
│ - Mobile-responsive CSS             │
│ - Submit button + forgot link       │
│ - Error message display             │
└─────────────────────────────────────┘

DETAILED (500 words)
┌─────────────────────────────────────┐
│ Act as a Software Engineer.         │
│                                     │
│ Task:                               │
│ Develop complete front-end code...  │
│                                     │
│ Requirements:                       │
│ - Technology Stack:                 │
│   - React (functional, Hooks)      │
│   - HTML5 semantic structure       │
│   - Plain CSS (no libraries)       │
│ - User Interface:                   │
│   - Clean, modern, responsive      │
│   - Mobile/tablet/desktop          │
│   - Email + Password fields        │
│   - Login button                   │
│   - Remember Me checkbox           │
│   - Forgot Password link           │
│   - Validation error messages      │
│   - General error display          │
│ - Functionality:                    │
│   - Client validation (regex)      │
│   - Password min 6 chars           │
│   - Disabled button until valid    │
│   - Async API simulation           │
│   - Success → redirect /dashboard  │
│   - Failure → show error           │
│ - Accessibility:                    │
│   - Semantic HTML5                 │
│   - ARIA attributes                │
│ - Security:                         │
│   - XSS prevention                 │
│   - No credential storage          │
│                                     │
│ Output:                             │
│ - LoginPage.js                      │
│ - LoginPage.css                     │
│ - App.js integration                │
│ - Well-commented code               │
└─────────────────────────────────────┘
```

---

**Now you have full control over prompt complexity!** 🎉
