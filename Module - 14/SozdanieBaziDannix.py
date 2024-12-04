import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('DELETE FROM Users') #очистка таблицы перед заполнением



users = [
    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000) for i in range(1, 11)
]
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)


cursor.execute('SELECT id FROM Users ORDER BY id')
ids = [row[0] for row in cursor.fetchall()]
if ids:
    cursor.execute('DELETE FROM Users WHERE id = ?', (ids[0],))

cursor.execute('SELECT id FROM Users ORDER BY id')
ids = [row[0] for row in cursor.fetchall()]


delete_ids = [ids[i] for i in range(2, len(ids), 3)]  # каждую третья запись удаляем
for user_id in delete_ids:
    cursor.execute('DELETE FROM Users WHERE id = ?', (user_id,))


cursor.execute('SELECT id FROM Users ORDER BY id')
ids = [row[0] for row in cursor.fetchall()]


for index in range(1, len(ids), 2):
    user_id = ids[index]
    cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (user_id,))


cursor.execute('UPDATE Users SET balance = 500 WHERE username = "User5"')


cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
ORDER BY id
''')
rows = cursor.fetchall()


for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")


connection.commit()
connection.close()