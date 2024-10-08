import threading
import random
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number  # пустой стол
        self.guest = None  # то, когда будет гость


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        eating_time = random.randint(3, 10)  # время, которое ест
        time.sleep(eating_time)  # поток ждет это время


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()  # очередь из гостей

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(guest)  # если нет свободных столов, то гость в очереди
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # стол стал свободныа

                    if not self.queue.empty():
                        next_guest = self.queue.get()  # берм гостя из очереди
                        table.guest = next_guest  # сажаем его за стол
                        next_guest.start()  # запускаем поток нового гостя
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)


tables = [Table(number) for number in range(1, 6)]  # созданеи 5 столов по дз
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya',
                'Alexandra']
guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
