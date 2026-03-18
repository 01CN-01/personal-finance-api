import sqlite3

def get_connection():
    conn = sqlite3.connect("data/finance.db", timeout=10)
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
        CREATE TABLE IF NOT EXISTS transactions(
        UUID TEXT PRIMARY KEY,
        user_UUID TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        description TEXT,
        amount REAL NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
    
    conn.commit()
    conn.close()

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
    user = cursor.fetchone()
    conn.close()
    
    return user

# TRANSACTIONS ------
def create_transactions(user_UUID, category_id, description, amount):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO transactions(user_UUID, category_id, description, amount)
        VALUES(?, ?, ?, ?, ?)
        """,(
           user_UUID,
           category_id,
           description,
           amount
        ))
    conn.commit()
    conn.close()

def delete_transaction(): # Finish
    print("continue")
    
def get_transactions(user_UUID):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT
            t.user_UUID,
            t.category_id,
            t.description,
            t.amount,
            t.created_at,
            c.category
        FROM
            transactions t
        JOIN 
            categories c ON t.category_id = c.ID
        WHERE
            t.user_UUID = ?
        """,(
            user_UUID,
        ))
    transactions = cursor.fetchall()
    conn.close()
    
    return transactions
    
# CATEGORIES ------
def make_category(category):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO categories(category)
            VALUES (?)
            """,(
                category,
                ))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_categories(): # Dropdown menu
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT * FROM categories
        """)
    categories = cursor.fetchall()
    conn.close()
    
    return categories

