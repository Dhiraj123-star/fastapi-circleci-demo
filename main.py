from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI + Docker + CircleCI!"}

@app.get("/health")
def health_check():
    return {"status":"ok"}