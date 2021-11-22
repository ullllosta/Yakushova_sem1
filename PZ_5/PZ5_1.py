# Найти сумму чисел ряда 1, 2, 3,..., 60 с использованием функции нахождения суммы.
# Использовать локальнын переменные.


def function_sum(a, b):
    sum = 0
    while a <= b:
        sum = sum + a
        a = a + 1
    return sum


first = float(input('Введите число, с которого начинается ряд: '))
last = float(input('Введите число, которым заканчивается ряд: '))
total = function_sum(first, last)
print('Сумма заданного ряда чисел: ', total)
