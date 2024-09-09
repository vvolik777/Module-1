import os  # для работы с операционной сис
import time  # для работы со временем

directory = "."  # '.' смотрим текущую папку

for root, dirs, files in os.walk(directory):  # пробегаемся по всем папкам/файлам помощью os.walk
    for file in files:
        filepath = os.path.join(root, file)  # получаем полный путь к файлу
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # форматируем время в удобный вид (день/месяц/год/ч:м)

        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)  # получаем род-ую директорию

        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
