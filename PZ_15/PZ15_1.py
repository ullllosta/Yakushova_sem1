# сгенерировать матрицу, в которой нечетные элементы заменяются на 0.


import random

n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
Matrix = [[random.randint(1, 5) for j in range(n)] for i in range(m)]

print('Изначальная матрица: ')
for i in Matrix:
    print(*i)


print('Измененная матрица: ')
res = lambda x: x % 2 == 1
for i in Matrix:                                          
    for j in i:
        if res(j):
            j = 0
        print(j, end=' ')
    print()


