# Организовать и вывести последовательность на N произвольных
# целых элементов, сформировать новую последовательность куда
# поместить квадраты четных элементов, найти их сумму и
# среднее арифметическое.


from _functools import reduce
from random import randint
N = int(input('Введите целое число, это будет длиной последовательности: '))
ListN = []
i = 0

while i < int(N):
    ListN.append(randint(1, 10))    # генерация исходного списка
    i += 1

new_ListN = list(filter(lambda x: x % 2 == 0, ListN))   # выбираем из списка четные элементы
p = list(map(lambda x: x**2, new_ListN))   # находим квадрат нечетных элементов, добавляем их в список p.

print('Исходный список: ', ListN)
print('Преобразованный список: ', p)
print('Сумма элементов списка: ', reduce(lambda x,y: x + y, p))
print('Среднее арифметическое элементов списка: ', reduce(lambda x,y: x + y, p) / len(p))