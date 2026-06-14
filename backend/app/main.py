from fastapi import FastAPI

app = FastAPI(title="RevMind Sales Chatbot")

@app.get("/")
def root():
    return {"message": "RevMind API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}