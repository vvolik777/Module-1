import re  # импорт регулярных выражений


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):  # возвращаем все слова из файлов в виде словаря
        all_words = {}  # пустой словарь для всех слов

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:  # with гарантия,что файл будет закрыт автоматически
                text = file.read().lower()

                text = re.sub(r'[.,!?;:=-]', '', text)  # убираем ненужные знаки препинания
                words = text.split()  # разбиваем строку текста на отдельные слова
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()

        word_positions = {}

        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1
            else:
                word_positions[file_name] = None

        return word_positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()

        word_counts = {}

        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)

        return word_counts


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('text'))
print(finder.count('text'))
