from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/api/products")
def get_products():
    conn = sqlite3.connect("novabite.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            product_name,
            ROUND(SUM(net_revenue_usd), 2) AS total_revenue,
            SUM(units_sold) AS units_sold
        FROM sales
        GROUP BY product_name
        ORDER BY total_revenue DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "product_name": row[0],
            "total_revenue": row[1],
            "units_sold": row[2]
        }
        for row in rows
    ]