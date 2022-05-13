import sqlite3

class SQLiter:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print('Вы пытаетесь записать в бд дубликат уникального ключа: ', e)

        return self.cursor.fetchall()

sqliter = SQLiter('lab_6.db')

sqliter.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, first_name TEXT);''')
sqliter.execute('''CREATE TABLE IF NOT EXISTS animals (id INTEGER PRIMARY KEY, name TEXT, kind TEXT);''')
sqliter.execute('''CREATE TABLE IF NOT EXISTS users_animals (id INTEGER PRIMARY KEY, user_id INTEGER, animal_id INTEGER);''')

sqliter.execute('''INSERT INTO users (id, first_name) VALUES (1, 'Вася');''')
sqliter.execute('''INSERT INTO users (id, first_name) VALUES (2, 'Петя');''')
sqliter.execute('''INSERT INTO users (id, first_name) VALUES (3, 'Маша');''')

print(sqliter.execute('''SELECT * FROM users;'''))

sqliter.execute('''INSERT INTO animals (id, name, kind) VALUES (1, 'Рональдо', 'Собака');''')
sqliter.execute('''INSERT INTO animals (id, name, kind) VALUES (2, 'Шарик', 'Собака');''')
sqliter.execute('''INSERT INTO animals (id, name, kind) VALUES (3, 'Клепа', 'Кошка');''')

print(sqliter.execute('''SELECT * FROM animals;'''))

sqliter.execute('''INSERT INTO users_animals (id, user_id, animal_id) VALUES (1, '1', '1');''')
sqliter.execute('''INSERT INTO users_animals (id, user_id, animal_id) VALUES (2, '1', '2');''')
sqliter.execute('''INSERT INTO users_animals (id, user_id, animal_id) VALUES (3, '2', '3');''')
sqliter.execute('''INSERT INTO users_animals (id, user_id, animal_id) VALUES (4, '3', '3');''')

print(sqliter.execute('''SELECT * FROM users_animals;'''))


# Выбрать из бд записи:
# 1 всех владельцев Клепы
# 2 всех животных Пети
# 3 всех пользователей которые владеют собаками