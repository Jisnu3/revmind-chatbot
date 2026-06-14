INTENT_QUERIES = {

    "top_region_revenue": """
    SELECT region,
           ROUND(SUM(net_revenue_usd),2) AS revenue
    FROM sales
    GROUP BY region
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "top_products": """
    SELECT product_name,
           ROUND(SUM(net_revenue_usd),2) AS revenue
    FROM sales
    GROUP BY product_name
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "sales_channel": """
    SELECT sales_channel,
           ROUND(SUM(net_revenue_usd),2) AS revenue
    FROM sales
    GROUP BY sales_channel
    ORDER BY revenue DESC
    """
}


def detect_intent(question):

    q = question.lower()

    if "region" in q and "revenue" in q:
        return "top_region_revenue"

    elif "product" in q:
        return "top_products"

    elif "channel" in q:
        return "sales_channel"

    return None