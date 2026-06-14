import sqlite3

conn = sqlite3.connect("novabite.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")

print(cursor.fetchone())

conn.close()
