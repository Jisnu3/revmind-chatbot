import sqlite3
import pandas as pd

CSV_PATH = "../data/novabite_sales_data.csv"
DB_PATH = "novabite.db"

df = pd.read_csv(CSV_PATH)

conn = sqlite3.connect(DB_PATH)

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM sales")

count = cursor.fetchone()[0]

print(f"Loaded {count} rows into SQLite")

conn.close()