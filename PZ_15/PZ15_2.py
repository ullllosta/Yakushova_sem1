
# В матрице элементы второго столбца заменить элементами из
# одномерного динамического массива соответствующей размерности.


import random

n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
Matrix = [[random.randint(-5, 5) for i in range(n)] for j in range(m)]

print('Изначальная матрица: ')
for i in Matrix:
    print(*i)

t = n
a = [0] * t
for i in range(t):
    a[i] = int(input('Введите элементы одномерного массива: '))

print('Полученный одномерный массив: ')
for i in a:
    print(i, end='')
print('\n')

for i in range(m):
    Matrix[i][1] = a[i]

print('Измененная матрица: ')
for i in Matrix:
    print(*i)