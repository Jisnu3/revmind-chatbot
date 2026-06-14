INTENT_QUERIES = {

    "top_region_revenue": """
    SELECT region,
           ROUND(SUM(net_revenue_usd),2) AS revenue
    FROM sales
    WHERE quarter='Q1-2024'
    GROUP BY region
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "snacks_margin": """
    SELECT
    ROUND(
        (SUM(gross_profit_usd) * 100.0) /
        SUM(net_revenue_usd),2
    ) AS margin
    FROM sales
    WHERE category='Snacks'
    """,

    "top_sales_rep_2025": """
    SELECT sales_rep,
           SUM(units_sold) AS units
    FROM sales
    WHERE date LIKE '2025%'
    GROUP BY sales_rep
    ORDER BY units DESC
    LIMIT 5
    """,

    "channel_comparison": """
    SELECT channel,
           ROUND(SUM(net_revenue_usd),2) AS revenue
    FROM sales
    WHERE channel IN ('E-Commerce','Modern Trade')
    GROUP BY channel
    ORDER BY revenue DESC
    """,

    "west_best_product": """
    SELECT product_name,
           ROUND(SUM(net_revenue_usd),2) AS revenue
    FROM sales
    WHERE region='West'
    GROUP BY product_name
    ORDER BY revenue DESC
    LIMIT 5
    """
}


def detect_intent(question):

    q = question.lower()

    if "region" in q and "q1" in q:
        return "top_region_revenue"

    elif "snacks" in q and "margin" in q:
        return "snacks_margin"

    elif "sales rep" in q and "2025" in q:
        return "top_sales_rep_2025"

    elif "e-commerce" in q and "modern trade" in q:
        return "channel_comparison"

    elif "west" in q and "product" in q:
        return "west_best_product"

    return None