#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    6
#    -> 5

N = int(input("Введите размер списка N: "))
a = list(range(1, N+1))
x = round(float(input('Введите любое число Х: ')))
close_num = 100
for i in range(len(a)):
    if a[i] < x:
        close_num = -close_num
    else:
        close_num = close_num + 0
    if a[i] >= x and a[i] - x <= close_num - x:
        close_num = a[i]
    elif a[i] <= x and close_num - x <= a[i] - x:
        close_num = a[i]
print(close_num)