import sqlite3

def init_db():

    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        complaint TEXT,
        category TEXT,
        priority TEXT,
        team TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()