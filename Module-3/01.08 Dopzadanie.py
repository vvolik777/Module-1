def calculate_structure_sum(data_structure):
    total_sum = 0  # переменная для хранения общей суммы

    def recursive_sum(data):  # вспомогательная функция для рекурс обхода данных
        nonlocal total_sum  # позволяем функции изменять внешнюю переменную
        if isinstance(data, list):
            for item in data:
                recursive_sum(item)  # рекурсивный вызов для каждого элемента

        elif isinstance(data, dict):
            for key, value in data.items():
                recursive_sum(key)  # рекурс вызов для ключа
                recursive_sum(value)  # рекурс вызов для значения

        elif isinstance(data, tuple):
            for item in data:
                recursive_sum(item)

        elif isinstance(data, set):  # если data - множество
            for item in data:
                recursive_sum(item)

        elif isinstance(data, str):  # если дата строка, добавляем ее длину к общей сумме
            total_sum += len(data)

        elif isinstance(data, (int, float)):  # если int/float, добавляем его к общей сумме
            total_sum += data

    recursive_sum(data_structure)

    return total_sum


# Входные данные (применение функции):
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
