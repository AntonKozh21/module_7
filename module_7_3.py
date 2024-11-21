import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation))
                words = text.split()
                all_words[filename] = words

        return all_words

    def find(self, word):
        word = word.lower()
        found = {}
        for name, words in self.get_all_words().items():
            if word in words:
                found[name] = words.index(word) + 1
        return found

    def count(self, word):
        word = word.lower()
        counts = {}
        for name, words in self.get_all_words().items():
            counts[name] = words.count(word)
        return counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
