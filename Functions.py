#1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def who_is(name,age,city):
    return  (f'{name}, {age} год(а), проживает в городе {city}' )

str1 = input('имя ')
str2 = input('возраст ')
str3 = input('город ')
print(who_is(str1,str2,str3))


