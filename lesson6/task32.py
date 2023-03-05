# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list_1=[]
n=int(input('Введите количество элементов массива: '))
for i in range(n):
    list_1.append(random.randint(-10,10))
print(list_1)
min_number = int(input('Минимальное число -> '))
max_number = int(input('Максимальное число -> '))
for i in range(len(list_1)):
	if min_number <= list_1[i] <= max_number:
		print('Номер индекса: ', i)