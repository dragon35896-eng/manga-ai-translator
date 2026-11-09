
from fastapi import FastAPI

app = FastAPI(
    title="Manga AI Translator",
    description="Backend API for manga translation",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Manga AI Translator server is running"
    }

@app.get("/health")
def health():
    return {"ok": True}
  
