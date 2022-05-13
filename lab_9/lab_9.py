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

sqliter = SQLiter('lab_9.db')

sqliter.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, car_id);''')
sqliter.execute('''CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY, model TEXT, color TEXT);''')

result = sqliter.execute('''SELECT * FROM cars;''')
print(result)
result = sqliter.execute('''INSERT INTO cars (id, model, color) VALUES (1, '', '')''')
print(result)

# Добавить в таблицу с машинами следующие данные:
# 1, '2107', 'Баклажан'
# 2, 'Ford Focus', 'Серебро'
# 3, 'Range Rover Sport', 'Мокрый асфальт'

# Добавить в таблицу с пользователями следующие данные:
# 1, 'Жорик', 3
# 2, 'Вася', 1
# 3, 'Петя', 2
# 4, 'Маша', 1
# 5, 'Наташа', 3

# Нужно будет вывести на экран информацию вида: Имя, Модель авто, Цвет

# Гугл:
# как создать таблицу sql
# как добавить данные в таблицу sql
# select sql синтаксис
# sql left join как написать
