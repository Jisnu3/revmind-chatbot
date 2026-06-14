from fastapi import FastAPI
from app.routes.products import router as products_router
from app.routes.summary import router as summary_router
from app.routes.trends import router as trends_router

app = FastAPI(title="RevMind Sales Chatbot")

app.include_router(products_router)
app.include_router(summary_router)
app.include_router(trends_router)
@app.get("/")
def root():
    return {"message": "RevMind API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}