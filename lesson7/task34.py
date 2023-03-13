# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def f(words):
    return sum(1 for i in words if i in 'аеёиоуыэюя')
poem = input('Введите фразу из стихотворения: ')
# poem = 'Хорошо_живет_на_светте_Винни_Пух, хорошо_поет_он_эти_песни_вслух' #Это чтобы не писать каждый раз, вводим стих вручную
string = poem.lower().split()
t = f(string[0])
if all([f(i) == t for i in string]):
    print('Парам пам-пам')
else:
    print('Пам парам')