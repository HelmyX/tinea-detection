import os
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Tinea API is running"}

@app.get("/health")
def health():
    return {"status": "ok", "key_set": "API_KEY" in os.environ}