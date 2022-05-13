# Есть некоторый аналог шахматной доски, на которой стоят шашки
row1 = ['W', None, 'W', None, 'W', None, 'W', None]
row2 = [None, 'W', None, 'W', None, 'W', None, 'W']
row3 = ['W', None, 'W', None, None, None, 'W', None]
row4 = [None, None, None, None, None, 'W', None, None]
row5 = [None, None, None, None, None, None, None, 'B']
row6 = ['B', None, 'B', None, 'B', None, None, None]
row7 = [None, 'B', None, 'B', None, 'B', None, 'B']
row8 = ['B', None, 'B', None, 'B', None, 'B', None]
columns = [row1, row2, row3, row4, row5, row6, row7, row8]

# Нужно написать двумерный цикл, который выводит на экран доску с шашками
# Однако None должны быть заменены на пробелы (каждый None на один пробел)
