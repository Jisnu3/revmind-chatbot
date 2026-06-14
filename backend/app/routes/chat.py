from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3

from app.query_planner import detect_intent, INTENT_QUERIES
from app.services.llm import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/api/chat")
def chat(request: ChatRequest):

    question = request.question

    intent = detect_intent(question)

    if not intent:
        return {
            "answer": "Sorry, I could not determine the analytics query."
        }

    conn = sqlite3.connect("novabite.db")
    cursor = conn.cursor()

    cursor.execute(INTENT_QUERIES[intent])

    rows = cursor.fetchall()
    if not rows:
        conn.close()
        return {
        "answer": "No matching data found."
        }

    conn.close()

    context = "\n".join(
        [f"{row[0]} = {row[1]}" for row in rows]
    )

    prompt = f"""
You are a business analytics assistant.

Question:
{question}

Data:
{context}

Answer using only supplied data.
"""

    answer = ask_gemini(prompt)


    print("Question:", question)
    print("Intent:", intent)
    print("Rows:", rows)
    print("Context:", context)
    print("Gemini Answer:", answer)
    return {
        "answer": answer
    }


