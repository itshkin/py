# Задача №1
"""1. На основе заготовленного кода напишите функцию print_friends_count() для вывода количества друзей. Аргументом
сделайте friends_count. Вызовите эту функцию не менее трёх раз с разными аргументами. Значениями friends_count могут
быть любые натуральные числа. """


# Решение
# объявите функцию здесь
def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


print_friends_count(1)
print_friends_count(2)
print_friends_count(7)

# Задача №2
"""Напишите цикл для запусков print_friends_count() c аргументами от 1 до 10."""


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


for count in range(11):
    print_friends_count(count)
