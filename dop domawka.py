def count_vse_glasnie_and_vse_soglasnie(quote):
    vse_glasnie = 'аеиоуыэюя'
    vse_soglasnie = 'бвгджзйклмнпрстфхцчшщ'

    print(quote)  # вывод исходной строки

    vse_glasnie_count = 0
    vse_soglasnie_count = 0

    for char in quote:
        if char.isalpha():
            if char.lower() in vse_glasnie:
                vse_glasnie_count += 1
            elif char.lower() in vse_soglasnie:
                vse_soglasnie_count += 1
    return vse_glasnie_count, vse_soglasnie_count


quote = 'Вдохновение - это умение приводить себя в рабочее состояние'
vse_glasnie, vse_soglasnie = count_vse_glasnie_and_vse_soglasnie(quote)
print(f'Гласных: {vse_glasnie}, Согласные: {vse_soglasnie}')