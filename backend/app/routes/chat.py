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

    Instructions:
    - Answer professionally.
    - Start with the direct answer.
    - If the question asks for top, highest, best, leading, or number one, return only the first result.
    - Only provide a ranked list when the user explicitly asks for multiple items.
    - Format revenue using $ and commas.
    - Do not use markdown.
    - Do not use Python tuples.
    - Do not use raw lists.
    - Use only supplied data.
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
            formatted_rows = []

            for row in rows:
                formatted_rows.append(
                    f"{row[0]} : {row[1]}"
                )

            fallback_answer = "\n".join(formatted_rows)

    elif intent == "west_best_product":
        fallback_answer  = (
            f"The best performing product in the West region is "
            f"{rows[0][0]} with revenue of ${rows[0][1]}."
        )
    elif intent == "top_sales_rep":
        fallback_answer = (
            f"The top sales representative is {rows[0][0]} "
            f"with total revenue of ${rows[0][1]:,.2f}."
        )
    elif intent == "top_category":
        fallback_answer = (
            f"The category with the highest revenue is {rows[0][0]} "
            f"with total revenue of ${rows[0][1]:,.2f}."
        )

    elif intent == "top_product":
        fallback_answer = (
            f"The product with the highest revenue is {rows[0][0]} "
            f"with total revenue of ${rows[0][1]:,.2f}."
        )

    elif intent == "top_region":
        fallback_answer = (
            f"The region with the highest revenue is {rows[0][0]} "
            f"with total revenue of ${rows[0][1]:,.2f}."
        )

    elif intent == "top_sales_channel":
        fallback_answer = (
            f"The highest revenue sales channel is {rows[0][0]} "
            f"with total revenue of ${rows[0][1]:,.2f}."
        )
    elif intent == "gross_profit_margin":
        fallback_answer = (
            f"The gross profit margin is {rows[0][0]}%."
        )

    elif intent == "total_revenue":
        fallback_answer = (
            f"The total revenue is ${rows[0][0]:,.2f}."
        )

    elif intent == "total_units_sold":
        fallback_answer = (
            f"A total of {rows[0][0]:,} units were sold."
        )

    elif intent == "top_5_products":

        lines = []

        for i, row in enumerate(rows, start=1):
            lines.append(
                f"{i}. {row[0]} - ${row[1]:,.2f}"
            )

        fallback_answer = "\n".join(lines)

    else:

        lines = []

        for i, row in enumerate(rows, start=1):

            if len(row) >= 2:
                lines.append(
                    f"{i}. {row[0]} - ${row[1]}"
                )

        fallback_answer = ( 
            "\n\n"
            + "\n".join(lines)
        )


    top_intents = [
        "top_sales_rep",
        "top_category",
        "top_product",
        "top_region",
        "top_region_revenue",
        "top_sales_channel",
        "west_best_product",
        "gross_profit_margin",
        "total_revenue",
        "total_units_sold"
    ]

    if intent in top_intents:
        answer = fallback_answer
    else:
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


