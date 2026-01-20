# Quick Start Guide

## Setup (First Time Only)

### 1. Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `backend\.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### 2. Frontend Setup
```bash
cd frontend
npm install
copy .env.example .env
```

## Running the Application

### Terminal 1 - Backend:
```bash
cd backend
venv\Scripts\activate
python main.py
```

### Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

Open browser to: http://localhost:3000

## Testing

Try entering: "Write code for login page"

The tool will automatically generate a structured, optimized prompt!
