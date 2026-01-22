# Quick Test Guide

## Testing Your Updated Prompt Improver

### 1. Start the Backend
```bash
cd backend
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 2. Start the Frontend
```bash
cd frontend
npm run dev
```

You should see:
```
VITE ready in XXX ms
Local: http://localhost:3000
```

### 3. Test the Feature

Open http://localhost:3000 in your browser.

#### Test Case 1: Simple Level
1. Enter: `Write code for login page`
2. Select: **Simple** radio button
3. Click: **Refine Prompt**
4. Expected: Short 2-4 sentence output

#### Test Case 2: Moderate Level (Default)
1. Enter: `Write code for login page`
2. Verify: **Moderate** is already selected
3. Click: **Refine Prompt**
4. Expected: Structured format with 4-5 requirements

#### Test Case 3: Detailed Level
1. Enter: `Write code for login page`
2. Select: **Detailed** radio button
3. Click: **Refine Prompt**
4. Expected: Comprehensive enterprise-level prompt (like before)

### 4. Visual Verification

✅ Check that the selected radio button:
- Has a purple gradient background
- Shows a checkmark (✓)
- Has purple text
- Has a purple border with glow

✅ Check that the detail selector appears between the textarea and buttons

### 5. API Testing (Optional)

Test the API directly:

```bash
# Test Simple
curl -X POST http://localhost:8000/api/refine \
  -H "Content-Type: application/json" \
  -d '{"raw_prompt": "Write code for login page", "detail_level": "simple"}'

# Test Moderate
curl -X POST http://localhost:8000/api/refine \
  -H "Content-Type: application/json" \
  -d '{"raw_prompt": "Write code for login page", "detail_level": "moderate"}'

# Test Detailed
curl -X POST http://localhost:8000/api/refine \
  -H "Content-Type: application/json" \
  -d '{"raw_prompt": "Write code for login page", "detail_level": "detailed"}'
```

### 6. Expected Results Summary

| Level | Output Length | Structure | Best For |
|-------|--------------|-----------|----------|
| Simple | 2-4 sentences | Paragraph | Quick tasks, GPT-3.5 |
| Moderate | ~100 words | Structured | Most use cases, GPT-4 |
| Detailed | ~200+ words | Comprehensive | Enterprise, complex projects |

---

## Troubleshooting

### Issue: No radio buttons visible
- **Fix**: Restart frontend with `npm run dev`

### Issue: API returns old format
- **Fix**: Restart backend with `python main.py`

### Issue: Default is "Simple" instead of "Moderate"
- **Fix**: Check App.jsx line where `useState('moderate')` is set

### Issue: Styling looks wrong
- **Fix**: Clear browser cache (Ctrl+Shift+R) or restart dev server

---

## Success Indicators ✅

- Radio buttons are visible and styled
- "Moderate" is selected by default
- Different levels produce different output lengths
- Selected option has visual feedback (checkmark, purple styling)
- No console errors in browser or terminal

---

**You're all set!** Your Prompt Improver now has flexible detail levels. 🎉
