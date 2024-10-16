import os
import time
from multiprocessing import Pool


def read_info(filename):
    all_data = []  # локальный список для хранения данных

    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    with open(filename, 'r') as file:  # открываем файл для чтения и построчно считываем данные
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()

    return all_data


def linear_read(filenames):  # линейный вызов для чтения файлов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейное выполнение заняло: {end_time - start_time:.6f} секунд")


def multiprocess_read(filenames):  # многопроцессорный вызов для чтения файлов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)  # параллельно вызываем функцию для каждого файла
    end_time = time.time()
    print(f"Многопроцессное выполнение заняло: {end_time - start_time:.6f} секунд")


if __name__ == "__main__":
    base_path = '/Users/vasilisa/Python/Module-1/Module-10/'
    filenames = [os.path.join(base_path, f'file {number}.txt') for number in range(1, 5)]

    print("Линейное выполнение:")
    linear_read(filenames)

    print("\nМногопроцессное выполнение:")
    multiprocess_read(filenames)
