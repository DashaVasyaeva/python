import os
import sys
import shutil
import re


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dir(path):
    try:
        os.mkdir(path)
        print(f'Директория {path} успешно создана')
    except FileExistsError:
        print(f'Директория {path} уже существует')


def remove_dir(path):
    try:
        os.removedirs(path)
        print(f'Директория {path} успешно удалена')
    except FileNotFoundError:
        print(f'Директория {path} не найдена')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def file_copy():
    filename = sys.argv[0]
    new_file = re.search(r'(\w+)\.[a-z]+', filename).group(1) + '_copy.py'
    shutil.copy(filename, new_file)
    print('Копия текущего файла создана')


if __name__ == '__main__':
    dir_path = 'dir_{}'
    [make_dir(dir_path.format(i)) for i in range(1, 10)]
    [remove_dir(dir_path.format(i)) for i in range(1, 10)]

    list_dir()
    file_copy()
