# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name — строка, полученная от пользователя,
# health = 100,
# damage = 50.
#
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

player={'name':input('player: '),'health':int(input('health: ')),'damage':int(input('damage: '))}
enemy={'name':input('enemy: '),'health':int(input('health: ')),'damage':int(input('damage: '))}
def attack(person1, person2):#person1-> person2
    person2['health']-=person1['damage']

print(player,enemy)
attack(enemy,player)
print(player,enemy)

print('После надажения', enemy['name'],'у',player['name'], 'останется health=',player['health'])