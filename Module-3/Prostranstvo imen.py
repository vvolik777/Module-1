calls = 0
def count_calls(): # Функция подсчитывающая вызовы остальных функций
    global calls #
    calls +=1

def string_info(string): #принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()  # Увеличиваем счётчик вызовов
    length = len(string)
    upper = string.upper() # верхний регистр
    lower = string.lower() # нижний регистр
    return (length, upper, lower)

def is_contains(string, list_to_search): #принимает два аргумента: строку и список
    count_calls()  # увеличиваем счётчик вызовов
    string = string.lower()  # приводим строку к нижнему регистру
    list_to_search = [item.lower() for item in list_to_search]  # Приводим все строки в списке к нижнему регистру
    return string in list_to_search  # Проверяем наличие строки в списке



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
