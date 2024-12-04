import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы, если её нет
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Очистка таблицы перед заполнением
cursor.execute('DELETE FROM Users')

# Добавление данных в таблицу
users = [
    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000) for i in range(1, 11)
]
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)
connection.commit()

# Удаление записи с id = 1
cursor.execute('SELECT id FROM Users ORDER BY id')
ids = [row[0] for row in cursor.fetchall()]
if ids:
    cursor.execute('DELETE FROM Users WHERE id = ?', (ids[0],))
connection.commit()

# Удаление каждой третьей записи
cursor.execute('SELECT id FROM Users ORDER BY id')
ids = [row[0] for row in cursor.fetchall()]
delete_ids = [ids[i] for i in range(2, len(ids), 3)]  # каждая третья запись
for user_id in delete_ids:
    cursor.execute('DELETE FROM Users WHERE id = ?', (user_id,))
connection.commit()

# Обновление баланса для каждого второго пользователя
cursor.execute('SELECT id FROM Users ORDER BY id')
ids = [row[0] for row in cursor.fetchall()]
for index in range(1, len(ids), 2):
    user_id = ids[index]
    cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (user_id,))
connection.commit()

# Установка баланса для пользователя с username = "User5"
cursor.execute('UPDATE Users SET balance = 500 WHERE username = "User5"')
connection.commit()

# Установка баланса для пользователя с id = 6
cursor.execute('UPDATE Users SET balance = 1000 WHERE id = 6')
connection.commit()

# Удаление записи с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')
connection.commit()

# Получение и отображение данных
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
ORDER BY id
''')
rows = cursor.fetchall()

for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

# Подсчет общего количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]

# Вычисление среднего баланса
average_balance = total_balance / total_users if total_users > 0 else 0

print(f"Общее количество пользователей: {total_users}")
print(f"Общая сумма балансов: {total_balance}")
print(f"Средний баланс: {average_balance:.1f}")

connection.close()
