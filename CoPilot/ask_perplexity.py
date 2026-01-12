import os
import requests


API_KEY = 'your-api-key-here'  # Replace with your actual Perplexity API key

headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

data = {
    "model": "sonar-reasoning",
    "stream": False,
    "max_tokens": 256,
    "messages": [
        {"role": "user", "content": "Tell me a joke."}
    ]
}

response = requests.post(
    'https://api.perplexity.ai/chat/completions',
    headers=headers,
    json=data
)

if response.ok:
    answer = response.json()["choices"][0]["message"]["content"]
    print("AI says:", answer)
else:
    print("Error:", response.status_code, response.text)