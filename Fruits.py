# Решить с помощью генераторов списка.
# 1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.
fr1=['яблоко','виноград','банан','киви','лимон']
fr2=['груша','яблоко','киви','слива','апельсин']
#через генератор списоков:
result= [fr for fr in fr1 for fruit in fr2 if fr==fruit]
print (result)

#классический способ
# result=[]
# # for fruit in fr2:
# #     for fr in fr1:
# #         #result=[fr for fr in fr1 if fr==fruit]
# #         if fr==fruit:
# #             result.append(fruit)
# # print (result)

