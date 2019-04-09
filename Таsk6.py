"""
@author: s.suvorova
3. Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
    Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
В этом случае ответ будет:
[5, 8]
"""
my_list = [2, 2, 5, 12, 8, 2, 12, 24, 24, 4, 5, 56, 56]
my_list_new=[]
# for i in range(len(my_list)):
#     for j in range(len(my_list)):
#         if i != j and my_list[i] == my_list[j]:
#             break
#     else:
#         my_list_new.append(my_list[i])
#print(my_list_new)
for i in range(len(my_list)):
    if my_list.count(my_list[i])==1 :
        my_list_new.append(my_list[i])
print(my_list_new)