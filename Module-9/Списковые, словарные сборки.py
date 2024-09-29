first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_strings if len(word) >= 5]  # длина строк не менее 5 символов
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if
                 len(word1) == len(word2)]  # пары слов одинаковой длины
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}  # чётная длина строки

print(first_result)
print(second_result)
print(third_result)
