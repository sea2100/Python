'''
1. Создайте класс Word.
2. Добавьте свойства text и part of speech.
3. Добавьте возможность создавать объект слово со значениями в скобках.
4. Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.'''
# NEXT!
# 1. Создайте классы Noun и Verb.
# 2. Настройте наследование от Word.
# 3. Добавьте защищенное свойство «Грамматические характеристики».
# 4. Перестройте работу метода show класса Sentence.
# 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.

class word:
    _gram_char = 0
    def __init__(self, text, part_of_speech):
        self.text = text  # само слово
        self.part_of_speech = part_of_speech  # часть речи


class sentence:
    words = {}  # словарь: номер слова и слово
    content = [1]  # список номеров слов в предложении

    def show(self, content):
        word_list = [self.words[i].text for i in content]  # получаем список слов
        sen = ' '.join(word_list)  # склеиваем предложение
        return sen  # возвращаем

    def show_part(self):
        part_list = [self.words[i]._gram_char for i in self.words.keys()]
        print(part_list)  # печать частей речи


    def __init__(self, words):
        self.words = words


class noun(word):
    _gram_char = 1
    def __init__(self, text):
        self.text = text  # само слово
        self.part_of_speech = 'noun'  # часть речи


class verb(word):
    _gram_char = 2
    def __init__(self, text):
        self.text = text  # само слово
        self.part_of_speech = 'verb'  # часть речи

word1 = noun('flag')
word2 = word('red', 'adjective')
word3 = word('I', 'pronaun')
word4 = verb('have')
word5= verb('make')
# print(word1.text, word2.text)
# print(word1.part_of_speech, word2.part_of_speech)

sen1 = sentence({1: word3, 2: word4, 3: word2, 4: word1, 5: word5 })
print(sen1.show([1, 2, 3, 4]))
print(sen1.show([1, 5, 3, 4]))
sen1.show_part()



