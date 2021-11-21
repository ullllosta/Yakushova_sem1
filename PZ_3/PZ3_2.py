# Даны три числа.
# Найти сумму двух наибольших из них.


a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')

while type(a) != float:      # проверка исключений
    try:
        a = float(a)
    except ValueError:
        print('Введено неправильное число :(')
        a = input('Введите первое число: ')

while type(b) != float:
    try:
        b = float(b)
    except ValueError:
        print('Введено неправильное число :(')
        b = input('Введите второе число: ')

while type(c) != float:
    try:
        c = float(c)
    except ValueError:
        print('Введено неправильное число :(')
        c = input('Введите третье число: ')

if (a <= b) and (a <= c):
    print('Ответ:', b + c)
elif (b <= a) and (b <= c):
    print('Ответ: ', a + c)
elif (c <= a) and (c <= b):
    print('Ответ: ', a + b)
