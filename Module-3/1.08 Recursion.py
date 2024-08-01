def get_multiplied_digits(number):
    str_number = str(number) # Преобразуем число в строку
    first = int(str_number[0]) # Берем первую цифру числа и преобразуем её обратно в целое число
    if len(str_number) > 1: # Если длина строки больше 1, то вызываем функцию рекурсивно
        return first * get_multiplied_digits(int(str_number[1:])) # Рекурсивный вызов функции для оставшихся цифр числа
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
