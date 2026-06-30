# Text-to-Image Service with FastAPI + Streamlit

## Overview
Production-ready generative AI service using `segmind/tiny-sd` (distilled Stable Diffusion) served via FastAPI with a Streamlit frontend.

## Architecture
- **models.py**: Loads and runs the diffusion pipeline
- **utils.py**: Image → byte stream conversion (no disk I/O)
- **main.py**: FastAPI endpoint `/generate/image`
- **client.py**: Interactive Streamlit UI

## Setup & Run
1. `pip install -r requirements.txt`
2. Terminal 1: `uvicorn main:app --reload --port 8000`
3. Terminal 2: `streamlit run client.py`

## Testing Prompts
- "Cyberpunk city at night, neon lights"
- "Oil painting of a peaceful forest"
- "Minimalist product photo of a futuristic smartphone"

## Business Use Case (Marketing Agency)
Accelerates ad concept brainstorming by generating dozens of visual variations in seconds, allowing creative teams to iterate faster and present more options to clients.

## Quality Control
Use **negative prompts** (e.g., "blurry, low quality, deformed") to maintain brand safety and output consistency in production environments.

**Tech**: FastAPI, Streamlit, Diffusers, PyTorch
