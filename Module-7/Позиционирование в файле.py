def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}  # пустой словарь, где будем хранить информацию о строках

        for i, string in enumerate(strings, start=1):
            position = file.tell()  # метод tell показывает, где в байтах начнется запись следующей строки
            file.write(string + '\n')
            strings_positions[(i, position)] = string  # добавляем информацию о строке в словарь

    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
