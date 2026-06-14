from fastapi import FastAPI
from app.routes.products import router as products_router
from app.routes.summary import router as summary_router
from app.routes.trends import router as trends_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router

app = FastAPI(title="RevMind Sales Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(products_router)
app.include_router(summary_router)
app.include_router(trends_router)
app.include_router(chat_router)
@app.get("/")
def root():
    return {"message": "RevMind API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}