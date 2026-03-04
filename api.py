from fastapi import FastAPI
import requests
from a2wsgi import ASGIMiddleware

app = FastAPI()

@app.get("/unmask")
def unmask(url: str):
    try:
        # Используем requests для надежной работы в среде cPanel
        resp = requests.head(url, allow_redirects=True, timeout=10)
        return {"original_url": url, "unmasked_url": resp.url}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def root():
    return {"status": "API is working from GitHub"}

# Этот адаптер обязателен для работы FastAPI на HostIQ
wsgi_app = ASGIMiddleware(app)
