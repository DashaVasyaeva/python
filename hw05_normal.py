from hw05_easy import make_dir, remove_dir
import sys
import os


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def print_help():
    print('help - получение справки')
    print('[1] [dir_name] - перейти в указанную папку')
    print('[2] - просмотреть содержимое текущей папки')
    print('[3] [dir_name] - удалить папку')
    print('[4] [dir_name] - создать папку')


def dir_change(path):
    try:
        os.chdir(path)
        print(f'Успешно перешел в директорию {path}')
    except FileNotFoundError:
        print(f'Директория {path} не существует')


def dir_contents():
    print([i for i in os.listdir()])


do = {
    'help': print_help,
    '1': dir_change,
    '2': dir_contents,
    '3': remove_dir,
    '4': make_dir
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key) and key in ('1', '3', '4'):
        do[key](dir_name)
    elif do.get(key) and key in ('2', 'help'):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
