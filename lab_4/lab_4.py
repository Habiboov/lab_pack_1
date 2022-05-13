# Нужно дописать класс, который используется для логирования событий в файл

from datetime import datetime

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def log_event_to_file(self, event):
        # если event не None, то:
        # создать строку с помощью функции make_log_row, записать в переменную
        # записать созданную строку с помощью функции open_file_and_write

    def make_log_row(self, event):
        # получить текущее время
        # создать строчку для записи в файл (время событие перенос_строки)
        # вернуть строчку с помощью инструкции return

    def open_file_and_write(self, row):
        # открыть файл для записи
        # записать строку в файл
        # закрыть файл


logger = Logger('logfile.txt')

logger.log_event_to_file('start')
logger.log_event_to_file('work')
logger.log_event_to_file('stop')