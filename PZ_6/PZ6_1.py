# Дан целочисленный список размера N.
# Увеличить все нечетные числа, содержащиеся в списке,
# на исходное значение последнего нечетного числа.
# Если нечетные числа в списке отсутствуют, то оставить список без изменений.


from random import randint

a = input('Введите размер списка: ')
ListN = []
i = 0

while i < int(a):                # генерация исходного списка
    ListN.append(randint(0, 100))
    i += 1
print('Изначальный список: ', ListN)


for ElementList in ListN:       # нахождение последнего нечетного элемента
    if ElementList % 2 == 1:
        k = ElementList
print('Последний нечетный элемент списка: ', k)


listTotal = []
for total in ListN:             # изменение нечентых значений списка
    if total % 2 == 1:
        listTotal.append(total + k)
    else:
        listTotal.append(total)
print('Измененный список: ', listTotal)

