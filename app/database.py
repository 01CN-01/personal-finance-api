import sqlite3
from app.models.user import RegisterCreate

def get_connection():
    conn = sqlite3.connect("data/finance.db")
    conn.row_factory = sqlite3.Row
    return conn
    

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            UUID TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            encrypted_password TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categories(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT UNIQUE NOT NULL
        )
        """)
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS  transactions(
        UUID TEXT PRIMARY KEY,
        user_UUID TEXT UNIQUE NOT NULL,
        category_id TEXT NOT NULL,
        description TEXT,
        amount REAL NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
    
    conn.commit()
    conn.close

# AUTHENTICATION ------
def create_account(user_UUID, first_name, last_name, email, hashed_password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(UUID, first_name, last_name, email, encrypted_password)
        VALUES(?, ?, ?, ?, ?)
        """,
        (user_UUID, first_name, last_name, email, hashed_password)
    )

    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT * FROM users WHERE email = ?
        """,(
            email,))
    
    return cursor.fetchone()

