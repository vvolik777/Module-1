import sqlite3

def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)
    connection.commit()
    connection.close()



def get_all_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products


def add_product(title, description, price):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
    """, (title, description, price))
    connection.commit()
    connection.close()
