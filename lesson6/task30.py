# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Первое число: '))
d = int(input('Второе число: '))
n = int(input('Третье число: '))
for i in range(n):
	print('an', '(',(i+1), ')', '= ', a1 + i * d)