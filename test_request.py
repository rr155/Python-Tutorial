import requests
resp = requests.post('http://127.0.0.1:7860/api/chat', json={'message':'Say hi'})
print('status', resp.status_code)
try:
    print(resp.json())
except Exception:
    print(resp.text)
