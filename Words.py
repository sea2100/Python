'''
1. Создайте класс Word.
2. Добавьте свойства text и part of speech.
3. Добавьте возможность создавать объект слово со значениями в скобках.
4. Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.'''
class word:
    text='any_word'
    part_of_speech='noun'           #по умолчанию существительное
    def __init__(self,text,pas):
        self.text=text              #само слово
        self.part_of_speech=pas     # часть речи

class sentence:
    words={}                        #словарь: номер слова и слово
    content=[1]                     #список номеров слов в предложении
    def show(self,content):
        word_list=[self.words[i].text for i in content]#получаем список слов
        sen=' '.join(word_list)     #склеиваем предложение
        return sen                  #возвращаем
    def show_part(self):
        part_list=[self.words[i].part_of_speech for i in self.words.keys()]
        print(part_list)            # печать частей речи
    def __init__(self,words):
        self.words=words


word1=word('flag','noun')
word2=word('red','adjective')
word3=word('I','pronaun')
word4=word('have','verb')
print(word1.text, word2.text)
print(word1.part_of_speech, word2.part_of_speech)

sen1=sentence({1:word3,2:word4,3:word2,4:word1})
print(sen1.show([1,3,2,4]))
sen1.show_part()



