import os
import re
import json
from flask import Flask, render_template, request, jsonify
import requests

APP_ROOT = os.path.dirname(__file__)
FALLBACK_ASK_FILE = os.path.join(APP_ROOT, "CoPilot", "ask_perplexity.py")

def parse_ask_file(path):
    """Parse API_KEY and default model from the provided ask_perplexity.py file.
    This avoids importing the file (which executes network calls at module import).
    Returns (api_key_or_none, model_or_none)
    """
    if not os.path.exists(path):
        return None, None
    text = open(path, "r", encoding="utf-8").read()
    key_m = re.search(r"API_KEY\s*=\s*['\"]([^'\"]+)['\"]", text)
    model_m = re.search(r'"model"\s*:\s*"([^\"]+)"', text)
    key = key_m.group(1).strip() if key_m else None
    model = model_m.group(1).strip() if model_m else None
    return key, model


API_KEY = os.getenv("PERPLEXITY_API_KEY") or os.getenv("API_KEY")
DEFAULT_MODEL = os.getenv("AI_MODEL")

if not API_KEY or not DEFAULT_MODEL:
    # attempt fallback parse
    fallback_key, fallback_model = parse_ask_file(FALLBACK_ASK_FILE)
    if not API_KEY:
        API_KEY = fallback_key
    if not DEFAULT_MODEL:
        DEFAULT_MODEL = fallback_model


if not API_KEY:
    raise RuntimeError(
        "No API key found. Set PERPLEXITY_API_KEY env var or place it in CoPilot/ask_perplexity.py"
    )

if not DEFAULT_MODEL:
    DEFAULT_MODEL = "sonar-reasoning"

app = Flask(__name__)


def call_perplexity_api(messages, model=None, max_tokens=256):
    model = model or DEFAULT_MODEL
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "model": model,
        "stream": False,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    if resp.ok:
        try:
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            return {"ok": True, "content": content, "raw": data}
        except Exception as e:
            return {"ok": False, "error": f"Malformed response: {e}", "raw_text": resp.text}
    else:
        return {"ok": False, "error": resp.text, "status_code": resp.status_code}


@app.route("/")
def index():
    return render_template("index.html", default_model=DEFAULT_MODEL)


@app.route("/api/chat", methods=["POST"])
def api_chat():
    body = request.get_json(force=True)
    user_message = body.get("message")
    messages = body.get("messages") or []
    model = body.get("model") or DEFAULT_MODEL
    max_tokens = body.get("max_tokens") or 256

    if not user_message and not messages:
        return jsonify({"error": "No message provided"}), 400

    # If only user_message is provided, construct minimal messages
    if not messages:
        messages = [{"role": "user", "content": user_message}]

    result = call_perplexity_api(messages, model=model, max_tokens=max_tokens)
    if result.get("ok"):
        return jsonify({"reply": result["content"]})
    else:
        return jsonify({"error": result.get("error", "unknown error"), "raw": result.get("raw")}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
