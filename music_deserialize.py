# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# Получить объект — словарь из предыдущего задания.

import json
with open('group.json','r') as f:
    my_favourite_group=json.load(f)#считываем объект
print(my_favourite_group)
print(type(my_favourite_group))#смотрим тип объекта

import pickle
with open('group.pickle','rb') as f:
    my_favourite_group2=pickle.load(f)#считываем объект
print(my_favourite_group2)
print(type(my_favourite_group2))#смотрим тип объекта
