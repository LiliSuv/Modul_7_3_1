class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        for file_names in self.file_names:
            with open (file_names, mode='w',encoding='utf-8') as file:
                file.write (data_text)
            with open (file_names, mode='r', encoding='utf-8') as file:
                a=file.read()
                word=''
                for wor in a:
                    word+=wor.lower()
                puncs = ',', '.', '=', '!', '?', ';', ':', ' - '
                for punc in puncs:
                    if punc in word:
                        word = word.replace (punc, ' ')
                        continue
                word = word.split ()
            all_words = {}
            all_words[file_names] = word
            return all_words

    def find(self, word):
        for key, value in self.get_all_words ().items ():
            finds = {}
            if word.lower () in value:
                finds[key] = value.index (word.lower ()) + 1
                return finds

    def count(self, word):
        counts = {}
        for value, key in self.get_all_words ().items ():
            words = key.count (word.lower ())
            counts[value] = words
            return counts


data_text = ("It's a text for task Найти везде.\n"
             " Используйте его для самопроверки.\n"
             " Успехов в решении задачи!\ntext,text,text")

finder2 = WordsFinder ('test_file.txt')
print (finder2.get_all_words ())
print (finder2.find ('TEXT'))
print (finder2.count ('teXT'))
