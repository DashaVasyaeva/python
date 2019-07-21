# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, digits):
    num = number * (10 ** digits)
    if num % 1 >= 0.5:
        num2 = (int(num) + 1) / (10 ** digits)
    else:
        num2 = int(num) / (10 ** digits)
    return "{:.{}f}".format(num2, digits)


n = float(input('Введите десятичное число: '))
n_digits = int(input('До какого разряда выполнить округление: '))
print(my_round(n, n_digits))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_list = []
    for i in ticket_number:
        ticket_list.append(int(i))
    if len(ticket_list) == 6:
        if sum(ticket_list[: 3]) == sum(ticket_list[-3:]):
            return True
        else:
            return False
    else:
        return 'Такого номера билета не существует'


ticket = input('Введите номер билета: ')
print(lucky_ticket(ticket))