import sqlite3
import bcrypt

# REGISTER
def register_user(name, email, password):
    conn = sqlite3.connect("database/pest.db")
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cursor.execute("INSERT INTO users VALUES (NULL,?,?,?,CURRENT_TIMESTAMP)",
                   (name, email, hashed))

    conn.commit()
    conn.close()

# LOGIN
def login_user(email, password):
    conn = sqlite3.connect("database/pest.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()

    conn.close()

    if user:
        if bcrypt.checkpw(password.encode(), user[3]):
            return user

    return None