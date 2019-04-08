#2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def max_num(num):
    return max(num)

numbers=[]
for i in range (3):
    numbers.append(int(input(f'введите число {i+1}: ')))
#print (numbers)
print ("Максимальное: ",max_num(numbers))

