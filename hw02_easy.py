# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз', 'абрикос', 'нектарин']
i = 0
while i < len(fruits):
    print(str(i + 1) + '. {:>10}'.format(fruits[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random

list_1 = []
list_2 = []
for i in range(10):
    list_1.append(random.randint(0,50))
    list_2.append(random.randint(0,50))
print('Первый список: ', list_1)
print('Второй список: ', list_2)
list_1_2 = list(set(list_1) - set(list_2))
print('Первый список без элементов, которые есть во втором: ', list_1_2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

new_list = []
for i in list_1_2: # Произвольный список для этой задачи взяла из задачи 2
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)
print('Новый список: ', new_list)
