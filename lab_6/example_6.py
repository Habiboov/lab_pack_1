# Чтобы научиться пользоваться SQL в полной мере, нужно научиться комбинировать данные из разных таблиц
# Так как в реляционных СУБД все данные хранятся в виде отдельных сущностей-таблиц, их нужно уметь объединять
# Воспользуемся классом из предыдущего примера для того, чтобы абстрагироваться от работы с конкретным модулем
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

db = SQLiter('test.db')

# Для начала создадим четыре таблицы и добавим в них тестовые данные
# Допустим у нас есть пользователи, которые могут состоять только в одной группе
# В этом случае мы просто добавляем в таблицу пользователей столбец с id группы, чтобы ее можно было указать
db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, first_name TEXT, group_id INTEGER);')
db.execute('CREATE TABLE IF NOT EXISTS user_groups (id INTEGER PRIMARY KEY, group_name TEXT);')

# Также допустим, что пользователи могут владеть машинами
# Но как один пользователь может владеть множеством машин, так и одна машина может принадлежать нескольким пользователям
# В этом случае мы создаем промежуточную таблицу для связи таблиц пользователей и машин
# Промежуточная таблица будет содержать поля с id пользователя и id машины
# Таким образом мы сможет задать соответствие между пользователями и машинами
db.execute('CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY, model TEXT, color TEXT);')
db.execute('CREATE TABLE IF NOT EXISTS users_cars (id INTEGER PRIMARY KEY, user_id INTEGER, car_id INTEGER);')

# Сперва создадим группы, в которых могут состоять пользователи
db.execute("INSERT INTO user_groups (id, group_name) VALUES (1, 'Группа Браво');")
db.execute("INSERT INTO user_groups (id, group_name) VALUES (2, 'Группа Стрелки');")
# Теперь создадим самих пользователей
# Вася будет состоять в группе Браво, Петя в группе Стрелки, а Маша вместе с Васей в группе Браво
# Названия и функционал несколько надуманы, но нужны для того, чтобы далее показать вам функционал JOIN
db.execute("INSERT INTO users (id, first_name, group_id) VALUES (1, 'Вася', 1);")
db.execute("INSERT INTO users (id, first_name, group_id) VALUES (2, 'Петя', 2);")
db.execute("INSERT INTO users (id, first_name, group_id) VALUES (3, 'Маша', 1);")
# Теперь добавим в БД автомобили
db.execute("INSERT INTO cars (id, model, color) VALUES (1, 'Нива', 'Мокрый баклажан');")
db.execute("INSERT INTO cars (id, model, color) VALUES (2, 'Ford Focus', 'Радужный металлик');")
# И привяжем автомобили к пользователям
# Пусть Вася владеет обеими машинами, Петя только первой, а Маша только второй
db.execute("INSERT INTO users_cars (id, user_id, car_id) VALUES (1, 1, 1);")
db.execute("INSERT INTO users_cars (id, user_id, car_id) VALUES (2, 1, 2);")
db.execute("INSERT INTO users_cars (id, user_id, car_id) VALUES (3, 2, 1);")
db.execute("INSERT INTO users_cars (id, user_id, car_id) VALUES (4, 3, 2);")

# Теперь давайте учиться соединять таблицы воедино для построения сложных запросов.
# Для этого воспользуемся операцией LEFT JOIN
# Сперва разберем простой вариант и выберем пользователей, состоящих в группе Браво
# Когда мы запрашиваем данные из нескольких  таблиц, нам нужно сперва указать имя таблицы, в которой лежит столбец
# И затем через точку мы указываем само имя столбца, который мы хотим добавить в выборку.
# Если столбцов много, то перечисляем все конструкции имя_таблицы.имя_столбца через запятую
# Чтобы выбрать данные с помощью LEFT JOIN напишем имя таблицы как обычно, после добавляем LEFT JOIN и название второй таблицы которую мы хотим объединить с первой
# Далее следует ключевое слово ON и условие по которому мы соединяем таблицы
# В нашем случае мы соединяем строки таким образом, что к строке из таблицы user_groups мы присоединяем строку из users
# в которых поле id из user_groups равно полю group_id из users

result = db.execute("""SELECT users.id, users.first_name FROM users 
LEFT JOIN user_groups ON user_groups.id = users.group_id
WHERE user_groups.group_name = 'Группа Браво';""")
print(result)

# Тройные кавычки - """ """ или ''' ''' также используются для объявления строк
# Их отличие в том, что мы можем использовать переносы строк внутри них в отличие от обычных кавечек - " " или ' '
# Важно, что сравнение строк регистрозависимо, то есть 'Группа Браво' и 'группа Браво' - это две разных строки

# Теперь давайте учиться делать более сложные объединения таблиц и выберем все машины, которые принадлежат Васе
# Обратите внимание на то, что если мы хотим выбрать все столбцы из определенной таблицы, то мы также можем использовать символ *
result = db.execute("""SELECT cars.* FROM cars 
LEFT JOIN users_cars ON cars.id = users_cars.car_id
LEFT JOIN users ON users.id = users_cars.user_id
WHERE users.first_name = 'Вася';""")
print(result)

# Загуглите остальные варианты операции JOIN, чтобы знать, как можно еще объединять данные друг с другом
