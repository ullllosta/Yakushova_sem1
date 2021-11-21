# Дано целое число N (N > 0)
# Определить, имеются ли в записи N нечетные цифры
# Если в записи числа имеются нечетные цифры, вывести True, если нет - False

N = input('Введите целое число больше 0: ')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введено неправильное число :(')
        N = input('Введите целое число больше 0: ')
    if int(N) <= 0:
        print('Введено неправильное число :(')
        N = input('Введите целое число больше 0: ')


param = False

while N != 0:
    ost = N % 10
    if ost % 2 == 1:
        param = True
        print(param)
        break
    else:
        N = N // 10

if param == False:
    print(param)
