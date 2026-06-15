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
    """,

    "top_category": """
    SELECT category,
           ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "top_product": """
    SELECT product_name,
           ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY product_name
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "top_region": """
    SELECT region,
           ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY region
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "top_sales_channel": """
    SELECT channel,
        ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY channel
    ORDER BY revenue DESC
    """,

    "top_sales_rep": """
    SELECT sales_rep,
           ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY sales_rep
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "quarter_revenue": """
    SELECT quarter,
           ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY quarter
    ORDER BY revenue DESC
    """,

    "top_subcategory": """
    SELECT subcategory,
           ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY subcategory
    ORDER BY revenue DESC
    LIMIT 5
    """,

    "category_profit": """
    SELECT category,
           ROUND(SUM(net_revenue_usd),2) revenue,
           ROUND(SUM(gross_profit_usd),2) profit
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC
    """,

    "monthly_revenue": """
    SELECT month,
           ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY month
    ORDER BY month
    """,

    "top_5_products": """
    SELECT product_name,
        ROUND(SUM(net_revenue_usd),2) revenue
    FROM sales
    GROUP BY product_name
    ORDER BY revenue DESC
    LIMIT 5
    """,
    "gross_profit_margin": """
    SELECT ROUND(
        (SUM(gross_profit_usd) * 100.0) /
        SUM(net_revenue_usd),2
    ) AS margin
    FROM sales
    """,

    "total_revenue": """
    SELECT ROUND(SUM(net_revenue_usd),2)
    FROM sales
    """,

    "total_units_sold": """
    SELECT SUM(units_sold)
    FROM sales
    """,

    "category_discount": """
    SELECT category,
           ROUND(AVG(discount_pct),2) avg_discount
    FROM sales
    GROUP BY category
    ORDER BY avg_discount DESC
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

    elif "top 5" in q and "product" in q:
        return "top_5_products"

    elif "west" in q and "product" in q:
        return "west_best_product"
    
    
    elif "category" in q and "revenue" in q:
        return "top_category"

    elif "product" in q and "revenue" in q:
        return "top_product"

    elif "region" in q and "revenue" in q:
        return "top_region"
    elif (
        "best performing products" in q
        or "top products" in q
        or "best products" in q
    ):
        return "top_5_products"

    elif "top performing region" in q:
        return "top_region"

    elif "gross profit margin" in q:
        return "gross_profit_margin"

    elif "total revenue" in q:
        return "total_revenue"

    elif "units sold" in q:
        return "total_units_sold"

    elif (
        "sales channel" in q
        or "revenue channel" in q
        or "channel performs best" in q
        or "most revenue" in q and "channel" in q
        or "highest revenue" in q and "channel" in q
    ):
        return "top_sales_channel"

    elif "sales rep" in q or "salesperson" in q:
        return "top_sales_rep"

    elif "quarter" in q:
        return "quarter_revenue"

    elif "subcategory" in q:
        return "top_subcategory"

    elif "profit" in q and "category" in q:
        return "category_profit"

    elif "month" in q and "revenue" in q:
        return "monthly_revenue"

    elif "discount" in q:
        return "category_discount"

    return None