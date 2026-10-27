# Capstone Deployment Runbook

## 1. Local Deployment (Development & Testing)

### Step 1: Environment Setup
```bash
git clone https://github.com/Gnath3144/GEN_AI_TRAINING.git
cd GEN_AI_TRAINING
python -m venv .venv
source .venv/bin/activate  # Or on Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
*(If running purely on local models, ensure `OLLAMA_HOST=http://localhost:11434` is accessible).*

### Step 3: Run Automated Test Verification
```bash
pytest capstone/tests/test_capstone.py -v
```

### Step 4: Launch Web Dashboard
```bash
streamlit run day-09/solutions/app.py
```

---

## 2. Containerized Deployment (Docker)
A production container can be built using Python 3.11-slim:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "day-09/solutions/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
Build and run:
```bash
docker build -t genai-intelligence-desk .
docker run -p 8501:8501 --env-file .env genai-intelligence-desk
```
