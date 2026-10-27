# Environment Setup Guide

This guide walks you through setting up your machine for the **10-Day LLM Engineering Course**. You can run all exercises either using **free local models (Ollama)** or **commercial cloud APIs (OpenAI, Gemini, Anthropic)**.

---

## 1. Prerequisites
- **Operating System**: Windows 10/11, macOS (Apple Silicon or Intel), or Linux (Ubuntu 22.04+).
- **Python**: Version 3.11 or 3.12 installed.
- **Git**: Installed and configured.
- **RAM**: Minimum 8 GB (16 GB recommended if running 3B+ parameter local models).

---

## 2. Fast Setup (Step-by-Step)

### Step 1: Clone the Training Repository
```bash
git clone https://github.com/Gnath3144/GEN_AI_TRAINING.git
cd GEN_AI_TRAINING
```

### Step 2: Create and Activate a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
*(If you encounter execution policy restrictions, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

**On macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 3. Local Model Runtime Setup (Ollama — Zero API Cost)

Ollama allows running open-source LLMs locally on your CPU/GPU without paying API fees or sending data to third parties.

1. Download and install Ollama from [ollama.com](https://ollama.com/download).
2. Start the Ollama service:
   - On Windows/macOS: Ollama launches as a system tray background app.
   - On Linux: Run `ollama serve`.
3. Pull a fast, lightweight model:
```bash
# Recommended default for most laptops:
ollama run llama3.2:1b

# If you have 16GB+ RAM:
ollama pull llama3.2:3b
```
4. Verify by running:
```bash
ollama list
```

---

## 4. API Key Configuration (Optional Cloud Track)

If you wish to test frontier cloud models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5/2.0):

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env     # macOS / Linux
copy .env.example .env   # Windows Command Prompt
Copy-Item .env.example .env # Windows PowerShell
```
2. Open `.env` and fill in whichever keys you have available:
```env
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=AIza...
ANTHROPIC_API_KEY=sk-ant-...
```
*Note: All day exercises are written with graceful fallbacks — if cloud API keys are absent, they automatically run against local Ollama.*

---

## 5. Verification Test

Run the pre-flight check script:
```bash
python -c "import openai, chromadb, sentence_transformers, ollama; print('Setup verified successfully!')"
```
You are ready to begin Day 01!
