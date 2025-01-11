import threading
from random import randint
from time import sleep
from queue import Queue
queue = Queue()

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe(*tables):
    def __init__(self, queue, *tables):
        self.queue = queue
        self.tables = []

    def guest_arrival(self, *guests):
        for guest in guests:
            if len(tables) < 5:
                queue = Queue()
                th1 = threading.Thread(target=Guest, args=(queue,), daemon=True)
                th1.start()
                print(f'сел(-а) за стол')


    def discuss_guests(self):
        while not queue.empty():

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()