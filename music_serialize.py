# 1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы

# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

my_favourite_group = {'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}
print (my_favourite_group)

import json
json_group=json.dumps(my_favourite_group)#преобразуем в строку json
print (json_group)
with open('group.json','w',encoding='utf-8') as f:
    json.dump(my_favourite_group,f)#Преобразуем и записываем файл
print('файл json записан')

import pickle
bgroups=pickle.dumps(my_favourite_group)
print(type(bgroups))#выводим тип
print(bgroups)# выводим сами байты
with open('group.pickle','wb') as fb:
    pickle.dump(my_favourite_group,fb)# записываем объект в файл
print('файл pickle записан')

