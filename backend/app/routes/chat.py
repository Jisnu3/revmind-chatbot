from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3
from app.services.llm import ask_gemini

from app.query_planner import detect_intent, INTENT_QUERIES

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

    if len(rows[0]) > 1:
        context = "\n".join(
            [f"{row[0]} = {row[1]}" for row in rows]
        )
    else:
        context = str(rows[0][0])



    prompt = f"""
    You are a business analytics assistant.

    Question:
    {question}

    Data:
    {context}

    Answer using only the supplied data.
    """


    if intent == "top_region_revenue":
        fallback_answer  = f"{rows[0][0]} had the highest net revenue in Q1 2024 with ${rows[0][1]}."

    elif intent == "snacks_margin":
        fallback_answer  = f"The gross profit margin for the Snacks category is {rows[0][0]}%."

    elif intent == "top_sales_rep_2025":
        fallback_answer  = f"{rows[0][0]} closed the most units in 2025 with {rows[0][1]} units sold."

    elif intent == "channel_comparison":
        if len(rows) >= 2:
            fallback_answer = (
                f"{rows[0][0]} generated ${rows[0][1]} revenue, "
                f"while {rows[1][0]} generated ${rows[1][1]} revenue."
            )
        else:
            fallback_answer = str(rows)

    elif intent == "west_best_product":
        fallback_answer  = (
            f"The best performing product in the West region is "
            f"{rows[0][0]} with revenue of ${rows[0][1]}."
        )

    else:
        fallback_answer  = str(rows)


    try:
        answer = ask_gemini(prompt)

    except Exception as e:
        print("Gemini Error:", e)

        answer = fallback_answer

    print("Question:", question)
    print("Intent:", intent)
    print("Rows:", rows)
    print("Context:", context)
    print("Final Answer:", answer)
    return {
        "answer": answer
    }


