from fastapi import FastAPI
from app.routes.products import router as products_router

app = FastAPI(title="RevMind Sales Chatbot")

app.include_router(products_router)

@app.get("/")
def root():
    return {"message": "RevMind API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}