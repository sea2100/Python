# 4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2
# (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# 1. Наносит урон. Это улучшенная версия функции из задачи 3.
# 2. Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его
# из здоровья персонажа.
player={'name':input('player: '),'health':int(input('health: ')),'damage':int(input('damage: ')),'armor':float(input('armor: '))}
enemy={'name':input('enemy: '),'health':int(input('health: ')),'damage':int(input('damage: ')),'armor':float(input('armor: '))}
def attack(person1, person2):#person1-> person2
    person2['health']-=calc_damage(person1['damage'],person2['armor'])#person1['damage']

def calc_damage(dam_attack, armor_defend):#берем вред нападающего и броню защищающегося
    return dam_attack/armor_defend

print('Сначала:',player,enemy)
attack(enemy,player)
print('После боя:',player,enemy)
print('После надажения', enemy['name'],'у',player['name'], 'останется health=',player['health'])
