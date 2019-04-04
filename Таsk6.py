"""
@author: s.suvorova
3. Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
    Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

В этом случае ответ будет:
[5, 8]
"""
#my_list = [2, 2, 5, 12, 8, 2, 12]
#my_new_list=list(set(my_list))
#print(my_list - my_new_list)

my_list = [2, 2, 5, 12, 8, 2, 12, 24, 24, 5, 4, 56, 56]
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if i != j and my_list[i] == my_list[j]:
            break
    else:
        print(my_list[i], end=' ')