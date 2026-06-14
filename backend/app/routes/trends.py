from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/api/trends")
def get_trends():
    conn = sqlite3.connect("novabite.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            month,
            ROUND(SUM(net_revenue_usd), 2) as revenue
        FROM sales
        GROUP BY month
        ORDER BY month
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "month": row[0],
            "revenue": row[1]
        }
        for row in rows
    ]