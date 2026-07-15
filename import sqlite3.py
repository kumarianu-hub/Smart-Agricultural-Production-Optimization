import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer TEXT NOT NULL,
    soil TEXT NOT NULL,
    season TEXT NOT NULL,
    area REAL NOT NULL,
    crop TEXT NOT NULL,
    yield REAL NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")