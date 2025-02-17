import sqlite3
from datetime import datetime

# Путь к базе данных
DB_PATH = "database/user_data.db"

# Функция для создания таблицы, если она еще не существует
def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Создание таблицы users, если она еще не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        language_code TEXT,
                        date_joined DATETIME,
                        last_active DATETIME,
                        interaction_count INTEGER,
                        state TEXT)''')
    conn.commit()
    conn.close()

# Функция для добавления или обновления данных пользователя
def upsert_user(user_id, username, first_name, last_name, language_code):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Проверяем, существует ли уже пользователь в базе
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    # Если пользователь существует, обновляем его данные
    if user:
        cursor.execute('''UPDATE users SET 
                          username = ?, 
                          first_name = ?, 
                          last_name = ?, 
                          language_code = ?, 
                          last_active = ?, 
                          interaction_count = interaction_count + 1
                          WHERE user_id = ?''',
                          (username, first_name, last_name, language_code, datetime.now(), user_id))
    else:
        # Если пользователя нет в базе, добавляем его
        cursor.execute('''INSERT INTO users (user_id, username, first_name, last_name, language_code, date_joined, last_active, interaction_count, state)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                          (user_id, username, first_name, last_name, language_code, datetime.now(), datetime.now(), 1, "start"))

    conn.commit()
    conn.close()

# Функция для получения данных о пользователе
def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()
    return user

# Функция для получения всех пользователей (например, для анализа)
def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return users
