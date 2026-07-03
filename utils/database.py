import sqlite3

conn = sqlite3.connect("database/history.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(

id INTEGER PRIMARY KEY AUTOINCREMENT,

pest TEXT,

confidence REAL,

severity TEXT

)
""")

conn.commit()

def save_history(pest, confidence, severity):

    cursor.execute(
        "INSERT INTO history(pest,confidence,severity) VALUES(?,?,?)",
        (pest, confidence, severity)
    )

    conn.commit() 