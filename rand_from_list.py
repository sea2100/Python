# 2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
import random
def rand_el(any_list):
    ln=len(any_list)
    if ln>0:
        result=any_list[random.randint(0,ln-1)]
    else: result=None
    return result

# list1=[1, 2, 3, 4, 5]
# list2=['s','d','f','g','h']
# list3=[]
# print(rand_el(list1))
# print(rand_el(list2))
# print(rand_el(list3))