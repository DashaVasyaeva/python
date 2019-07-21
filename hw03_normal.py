# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fibonacci_list = [1, 1]
    while len(fibonacci_list) <= m:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list[n - 1: m]


first = int(input('С какого элемента показать ряд Фибоначчи: '))
last = int(input('По какой элемент показать ряд Фибоначчи: '))
print(fibonacci(first, last))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = len(origin_list)
    for i in range(n-1):
        for j in range(n - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list


print('Отсортированный список по возрастанию: ', sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(my_func, iterable):
    new_iterables = []
    for i in iterable:
        if my_func(i):
            new_iterables.append(i)
    print('Исходный элемент: ', iterable)
    return new_iterables


def func(x):
    if x > 0:
        return True


print('Отфильтрованный: ', my_filter(func, [-92, 10, -3.4, 2, 20, -1, 4, 10, 0]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogram(*args):
    a = []
    for i in args:
        a.append(i)
    a.sort()
    print('Координаты точек: ', a)
    if a[0][0] + a[3][0] == a[1][0] +a[2][0] and a[0][1] + a[3][1] == a[1][1] + a[2][1]:
        return True
    else:
        return False


a1 = [-3, -2]
a2 = [-4, -7]
a3 = [-9, -8]
a4 = [-8, -3]
print(parallelogram(a1, a2, a3, a4))
