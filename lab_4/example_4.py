# __________________ Написание классов __________________
# Так как мне написать свой класс? Просто!
# Пишем ключевое слово class, затем название класса, двоеточие и перечисляем все функции внутри класса.
# В функции, выполняющейся при создании объекта (конструкторе) также нужно создать все атрибуты(свойства) объекта.
# Атрибуты объекта - это... другие объекты, либо примитивы (которые, если разобраться - тоже объекты)

class EmptyClass:
    def __init__(self):
        self.attribute = None


# Вот я создал пустой класс и в объекте этого класса один атрибут.
# Функция __init__(self) это конструктор класса. Данная функция выполняется всегда при создании экземпляра класса.

# Функции, находящиеся внутри класса отличаются от иных тем, что у них всегда должен быть как минимум один аргумент.
# Первый аргумент функций, находящихся внутри класса, всегда указывает на сам экземпляр класса.
# Традиционно его называют "self".
# Зачем? Это такой "маяк", позволяющий функциям и атрибутам внутри одного класса взаимодействовать друг с другом.
# С помощью self функции внутри одного объекта (одного класса) сохраняют в атрибутах данные и вызывают друг друга.
# Таким образом мы скрываем (инкапсулируем) сложные расчёты внутри объекта от использующего объект человека.

class TestClass:
    def func_one(self):
        print('Я первая функция класса')

    def func_two(self):
        print('А я вторая функция класса, которая вызывает первую через self')
        self.func_one()


# Обратите внимание, что во-первых вам не обязательно переопределять конструктор.
# Если вы не переопределили стандартный конструктор, объект все равно будет создан.
# Во-вторых при вызове функций внутри класса вам не нужно передавать в них первый аргумент.
# Он подставляется автоматически!
# Также вам не обязательно передавать первый аргумент при вызове функции из действующего объекта. (Об этом далее)

# Давайте теперь научимся создавать экземпляры класса (объекты) и разберемся как оно все работает.
# Заведем еще один пример класса:
class TestClassTwo:
    # Обратите внимание, что конструктор принимает внутрь себя один аргумент (self не считается)
    def __init__(self, given_attribute):
        self.attribute = given_attribute

    def print_func(self):
        print(self.attribute)

    def change_func(self, new_attribute):
        self.attribute = new_attribute


# __________________ Создание экземпляров класса __________________
# Чтобы создать экземпляр класса, надо вызвать его конструктор и он вернёт готовый экземпляр.
# Конструктор вызывается с помощью скобочек () после имени класса.
test_class_instance = TestClass()

# Если в конструктор надо передать аргумент, то надо поместить передаваемый объект (объекты) в скобки
test_class_two_instance = TestClassTwo('Я аргумент, который передается в конструктор')

print('Вызываем функции из первого класса:')
# Вызовем функцию func_one из объекта класса TestClass
test_class_instance.func_one()
# А теперь вызовем функцию func_two из объекта класса TestClass, которая в свою очередь еще и вызовет func_one
test_class_instance.func_two()
# Обратите внимание, что при вызове функции из действующего экземпляра, нам не нужно передавать первый аргумент

print('Вызываем функции из второго класса:')
# Теперь давайте разбираться с атрибутами, выведем текущее значение атрибута self.attribute второго экземпляра на экран
test_class_two_instance.print_func()
# Теперь запишем в этот атрибут новое значение
test_class_two_instance.change_func('Я новое значение атрибута')
# И снова выведем текущее значение атрибута self.attribute на экран
test_class_two_instance.print_func()

# Атрибут изменил свое значение на новое. Старого значения больше нет.
# Обратите внимание на то, что внутри класса функции обмениваются информацией через атрибуты.
# Функции вне классов могут обмениваться информацией через аргументы и возвращаемые значения.

# Функции все классов НЕ ДОЛЖНЫ обмениваться информацией через изменение глобальных переменных, подражая классовым.
# Почему? Потому что это усложняет логику программ и вызывает плавающие ошибки в работе ПО, которые сложно найти.

# __________________ Наследование от класса __________________
print('__ Наследование от класса __')
# Чтобы унаследоваться от какого-либо класса, мы просто указываем его в скобках после названия создаваемого класса
# При этом можно переопределить существующие внутри родительского класса функции
class TestClassChild(TestClass):
    def func_two(self):
        print('Я новая вторая функция')
        self.func_one()

test_class_child_instance = TestClassChild()
test_class_child_instance.func_two()
# Как вы видите, в этом случае функция func_one вызывается из класса-родителя, а именно из класса TestClass

# Можно наследоваться от нескольких классов.
# Если при этом в этих классах существуют функции с одинаковыми названиями, то будет использован поиск в ширину
# Загуглите алгоритмы обхода в ширину и в глубину, это все равно пригодится вам при программировании
# Сначала будет поиск функции в B, потом в C, и уже после этого в A (B унаследованна от A)
print('Наследование от нескольких классов:')
class A:
    def hi(self):
        print("A")

class B(A):
    def hi(self):
        print("B")

class C(A):
    def hi(self):
        print("C")

class D(B, C):
    pass

d = D()
d.hi()
# Как вы видите, на экране буква B, потому что класс B был указан первым и внутри него нашлась функция hi
# Если бы ее там не было, то мы увидели бы на экране C
# Если бы и в C не было такой функции, то мы увидели бы на экране A


# __________________ послесловие __________________
# В прошлой лабораторной я рассказывал вам про конструкцию with ... as
# Вы в своем классе можете переопределить не только конструктор (функция __init__), но и прочие стандартные функции
# Их внушительное множество, вы можете посмотреть на них здесь https://pythonworld.ru/osnovy/peregruzka-operatorov.html

# Вы можете переопределить внутри вашего класса функции __enter__ и __exit__
# Они автоматически вызываются конструкцией with ... as
# __enter__ вызывается в начале, а __exit__ вызывается в конце (даже при возникновении исключения)
# В потоках работы с файлами эти функции уже определены разработчиками питона и __exit__ закрывает поток в любом случае
# Поэтому with open("ваш файл", "r") as file: гораздо безопаснее и предпочтительнее в использовании
# По пути чтения или записи в файл может произойти исключение и менеджер контекстов закроет поток в любом случае

# Погуглите про менеджер контекстов, чтобы расширить свой кругозор