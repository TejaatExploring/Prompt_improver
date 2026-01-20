# 🆓 FREE Setup Guide - Using Google Gemini API

## Why Google Gemini?
- **Completely FREE** for personal use
- Generous free tier (1500 requests per day)
- Fast and powerful AI
- No credit card required

---

## Step-by-Step Setup

### 1. Get Your FREE Gemini API Key

1. **Visit**: https://aistudio.google.com/app/apikey
2. **Sign in** with your Google account
3. **Click** "Create API Key"
4. **Copy** the API key (starts with `AIza...`)

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

This will install both Gemini and OpenAI libraries (you'll only use Gemini).

### 3. Configure Your API Key

Edit `backend\.env` and paste your Gemini API key:

```env
API_PROVIDER=gemini
GEMINI_API_KEY=AIzaSy...your_actual_key_here
MODEL_NAME=gemini-1.5-flash
```

### 4. Start the Backend

```bash
# Make sure you're in the backend folder with venv activated
cd backend
venv\Scripts\activate
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 5. Start the Frontend

Open a **new terminal**:

```bash
cd frontend
npm run dev
```

### 6. Test It!

1. Open http://localhost:3000
2. Enter: "Write code for login page"
3. Click "Refine Prompt"
4. ✅ It works!

---

## Troubleshooting

### Error: "Gemini API key not configured"
- Make sure you copied the full API key (starts with `AIza`)
- Check that `backend\.env` has `API_PROVIDER=gemini`
- Restart the backend server after editing .env

### Error: "Module not found"
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### Gemini API Limits
- **Free tier**: 1500 requests/day
- **Rate limit**: 60 requests/minute
- If you hit limits, wait 1 minute and try again

---

## Switching Between Gemini and OpenAI

Edit `backend\.env`:

**For FREE Gemini:**
```env
API_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_key
```

**For OpenAI (paid):**
```env
API_PROVIDER=openai
OPENAI_API_KEY=your_openai_key
```

---

## Free Tier Comparison

| Provider | Cost | Free Tier | Speed | Quality |
|----------|------|-----------|-------|---------|
| **Google Gemini** | FREE | 1500/day | Fast | Excellent |
| OpenAI | Paid | $5 credit (new accounts) | Very Fast | Excellent |

**Recommendation**: Use Gemini for this project - it's free and works great!

---

## Still Need Help?

1. Verify your Gemini API key at: https://aistudio.google.com/app/apikey
2. Make sure `backend\.env` exists (not `.env.example`)
3. Check that venv is activated (you should see `(venv)` in your terminal)
4. Restart the backend server after any .env changes

---

**You're all set! Enjoy your FREE AI-powered prompt refinement tool! 🎉**
