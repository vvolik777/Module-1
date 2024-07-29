def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()

    for word in other_words:
        word = word.lower()

        if root_word in word or word in root_word: # Проверяем, содержит ли текущее слово word корень root_word или наоборот
            same_words.append(word) # если условие выполняется, добавляем слово в список same_words

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')


print(result1)
print(result2)
