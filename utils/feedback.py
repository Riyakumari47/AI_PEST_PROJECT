import sqlite3

conn = sqlite3.connect("database/pest.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(

id INTEGER PRIMARY KEY AUTOINCREMENT,

pest TEXT,

feedback TEXT

)
""")

conn.commit()


def save_feedback(pest, feedback):

    cursor.execute(
        "INSERT INTO feedback(pest,feedback) VALUES(?,?)",
        (pest, feedback)
    )

    conn.commit()