# AI Chat Portal (Flask)

This repository contains a small Flask-based AI chat portal that forwards messages to the Perplexity AI chat completions endpoint.

Quick start

1. Install dependencies (prefer a virtualenv):

   python -m venv .venv; .venv\Scripts\Activate; pip install -r requirements.txt

2. Set your API key (recommended) as an environment variable in PowerShell:

   $env:PERPLEXITY_API_KEY = 'your_api_key_here'

   Optionally you can set `AI_MODEL` to change the default model name.

   If you don't set env vars, the app will attempt to read `CoPilot/ask_perplexity.py` and extract the API key and model from it.

3. Run the app:

   python app.py

4. Open http://127.0.0.1:7860 in your browser.

Notes
- The app is intentionally small and synchronous. For production usage you should add streaming, user sessions, authentication, rate-limiting and error handling.
