import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # cоздание таблицы products
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    # создание таблицы Users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if cursor.fetchone() is None:
        cursor.execute("""
            INSERT INTO Users (username, email, age, balance) 
            VALUES (?, ?, ?, ?)
        """, (username, email, age, 1000))  # по дз баланс 1000
        connection.commit()
        print(f"Пользователь {username} добавлен в базу данных.")
    else:
        print(f"Пользователь с именем {username} уже существует в базе данных.")

    connection.close()


def is_included(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.close()

    return user is not None


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    print(f"Извлеченные продукты: {products}")

    connection.close()
    return products


def add_product(title, description, price):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products WHERE title = ?", (title,))
    if cursor.fetchone() is None:
        cursor.execute("""
            INSERT INTO Products (title, description, price) 
            VALUES (?, ?, ?)
        """, (title, description, price))
        connection.commit()
        print(f"Продукт {title} добавлен в базу данных.")
    else:
        print(f"Продукт с названием {title} уже существует в базе данных.")

    connection.close()
