import threading
import time

# для предотвращения смешивание вывода разных потоков в консоли создаем глобальный объект блокировки
lock = threading.Lock()


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        with lock:  # блокируем вывод для каждого рыцаря по очереди
            print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            self.days += 1
            self.enemies -= self.power
            remaining_enemies = max(self.enemies, 0)

            with lock:
                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")
            time.sleep(1)  # один день сражения =1 секунда

        with lock:
            print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)  # 1й рыцарь с силой 10
    second_knight = Knight('Sir Galahad', 20)  # 2й рыцарь с силой 20

    #
    first_knight.start()
    time.sleep(0.5)  # пауза для чередования действий рыцарей
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
