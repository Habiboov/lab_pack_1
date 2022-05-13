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

db = SQLiter('lab_5.db')

db.execute('''CREATE TABLE cats (id INTEGER PRIMARY KEY, name TEXT, color TEXT);''')
# У вас есть класс для работы с БД и пример его использования, ниже нужно выполнить задание

# Нужно создать 4 строки:
# id - 1, name - Борис, color - Рыжий
# id - 2, name - Клёпа, color - Белый
# id - 3, name - Мурзик, color - Черный
# id - 4, name - Масяня, color - Кремовый

# Запросить из БД строки в которых id > 2 и (имя 'Клёпа' или цвет 'Черный')
# Запросить из БД имена животных, у которых цвет Белый

# Обновить строчку, в которой color='Кремовый', задать в ней color='Кремово-Желтый'