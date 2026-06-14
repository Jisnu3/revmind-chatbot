from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/api/summary")
def get_summary():
    conn = sqlite3.connect("novabite.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            ROUND(SUM(net_revenue_usd), 2),
            SUM(units_sold),
            ROUND(
                (SUM(gross_profit_usd) * 100.0) /
                SUM(net_revenue_usd), 2
            )
        FROM sales
    """)

    total_net_revenue, total_units, gross_profit_margin = cursor.fetchone()

    cursor.execute("""
        SELECT region
        FROM sales
        GROUP BY region
        ORDER BY SUM(net_revenue_usd) DESC
        LIMIT 1
    """)
    top_region = cursor.fetchone()[0]

    cursor.execute("""
        SELECT channel
        FROM sales
        GROUP BY channel
        ORDER BY SUM(net_revenue_usd) DESC
        LIMIT 1
    """)
    top_channel = cursor.fetchone()[0]

    cursor.execute("""
        SELECT product_name
        FROM sales
        GROUP BY product_name
        ORDER BY SUM(net_revenue_usd) DESC
        LIMIT 1
    """)
    top_product = cursor.fetchone()[0]

    conn.close()

    return {
        "total_net_revenue": total_net_revenue,
        "total_units": total_units,
        "gross_profit_margin": gross_profit_margin,
        "top_region": top_region,
        "top_channel": top_channel,
        "top_product": top_product
    }