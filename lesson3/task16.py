#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    3
#    -> 1

n = int(input('Введите длину массива N: '))
x = int(input('Введите некоторе число X: '))
def masgen(n):
  for i in range(1,n):
    list.append(i)
  print('Исходный массив -> ', list)
  print('Количество чисел Х=', x, 'в массиве -> ',list.count(x))
list=[]
masgen(n)