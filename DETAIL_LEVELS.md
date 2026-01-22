# Detail Levels Guide

Your Prompt Improver now offers **3 levels of detail** to match different use cases and model capabilities.

## 📋 Detail Level Options

### 1️⃣ **Simple** - Quick & Concise
**Best for:**
- Quick tasks and simple requests
- Lower-tier models (GPT-3.5, Claude Haiku, Gemini Flash)
- Users who want minimal changes
- Time-sensitive prompts

**Output:** 2-4 sentences with role, task, and 1-2 key requirements

**Example Input:** `Write code for login page`

**Example Output:**
```
Act as a Front-end Developer. Create a responsive login page component using React and CSS. Include email/password fields, form validation, and a submit button. The design should be clean and mobile-friendly.
```

---

### 2️⃣ **Moderate** - Balanced (Default, Recommended)
**Best for:**
- Most general use cases
- Mid-tier models (GPT-4, Claude Sonnet, Gemini Pro)
- Balancing clarity without overwhelming
- Professional projects

**Output:** Structured with role, task description, 4-5 essential requirements

**Example Input:** `Write code for login page`

**Example Output:**
```
Act as a Front-end Developer.

Task: Create a modern, responsive login page component for a React application.

Requirements:
- Use React functional components with hooks
- Include email and password input fields with validation
- Implement a clean, mobile-responsive design using CSS
- Add a submit button and "Forgot Password?" link
- Display error messages for invalid inputs

The code should be ready to integrate and follow React best practices.
```

---

### 3️⃣ **Detailed** - Comprehensive
**Best for:**
- Complex enterprise projects
- High-end models (GPT-4, Claude Opus, Gemini Ultra)
- When you need maximum specifications
- Production-ready requirements

**Output:** Extensive structured format with comprehensive requirements, edge cases, best practices

**Example Input:** `Write code for login page`

**Example Output:**
```
Act as a Senior Front-end Developer.

Task:
Develop the complete front-end code for a modern, responsive user login page component, ready for integration into a React application.

Requirements:
- **Technology Stack**: Use React (functional components with Hooks), HTML5, and plain CSS
- **UI Components**: Email/password fields, Login button, "Remember Me" checkbox, "Forgot Password?" link
- **Validation**: Client-side email format validation (regex) and password length (min 6 chars)
- **Error Handling**: Display field-specific validation errors and general login failure messages
- **Responsiveness**: Adapt to mobile, tablet, and desktop screen sizes
- **Accessibility**: Use semantic HTML5 and ARIA attributes for screen readers
- **API Simulation**: Simulate POST /api/login with success/failure handling
- **Best Practices**: Follow React conventions, componentization, and clean code principles

Output:
- Complete React component code (LoginPage.jsx)
- Dedicated CSS file (LoginPage.css)
- Example integration in App.js
- Well-commented code with clear structure
```

---

## 💡 How to Choose

| Your Need | Recommended Level |
|-----------|------------------|
| Quick prototype or simple task | **Simple** |
| Most projects & general use | **Moderate** ⭐ |
| Enterprise/complex requirements | **Detailed** |
| Using GPT-3.5 / Claude Haiku | **Simple** |
| Using GPT-4 / Claude Sonnet | **Moderate** ⭐ |
| Using top-tier models | **Detailed** |
| Teaching beginners | **Simple** or **Moderate** |
| Production systems | **Detailed** |

---

## 🎯 Default Setting

The tool defaults to **Moderate** level, which provides the best balance for most users and models. It's detailed enough to get good results but not so overwhelming that it confuses users or lower-tier models.

---

## 🔄 How to Use

1. Enter your raw prompt
2. Select your preferred detail level (Simple, Moderate, or Detailed)
3. Click "Refine Prompt"
4. Copy and use the improved prompt with your favorite LLM

---

**Note:** You can always try different levels to see which works best for your specific use case!
