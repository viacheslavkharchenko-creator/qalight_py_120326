import sqlite3

# Створення/підключення до бази даних
def get_db_instance(db_path: str  = 'test_database.db'):
    with sqlite3.connect(db_path) as conn:
        # Створення курсора для виконання SQL-запитів
        cursor = conn.cursor()
        return cursor, conn

def get_data(cursor):
    # Виконання запиту
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    return data

# # Закриття з'єднання
# conn.close()
db_path = 'test_database.db'
cursor, conn = get_db_instance(db_path)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
# conn.commit()

# cursor.execute('''
#     INSERT INTO users (username, email, age) 
#     VALUES (?, ?, ?)
# ''', ('Yevhen', 'yevhen@example.com', 25))
# users_data = [
#     ('alice', 'alice@example.com', 30),
#     ('bob', 'bob@example.com', 28),
#     ('charlie', 'charlie@example.com', 35)
# ]

# cursor.executemany('''
#     INSERT INTO users (username, email, age) 
#     VALUES (?, ?, ?)
# ''', users_data)


conn.commit()
all_user = get_data(cursor)
print(all_user)