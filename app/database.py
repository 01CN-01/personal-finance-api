import sqlite3
import uuid



user_UUID = str(uuid.uuid4())

def get_connection():
    conn = sqlite3.connect("data/finance.db")
    conn.row_factory = sqlite3.Row
    
# ------ USER ------
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
        CREATE TABLE IF NOT EXITS categories(
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            category TEXT UNIQUE NOT NULL
        )
        """)
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXITS  transactions(
        UUID TEXT PRIMARY KEY,
        user_UUID TEXT UNIQUE NOT NULL,
        category_id TEXT NOT NULL,
        description TEXT,
        amount REAL, NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
    
    conn.commit()
    conn.close