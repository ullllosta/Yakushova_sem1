# Описать функцию SortInc3(A, B, C), меняющую содержимое переменных A, B, C
# таким образом, чтобы их значения оказались упорядоченными по возрастанию
# (A, B, C - вещественные параметры, являющиеся сразу входными и выходными)
# С помощью этой функции упорядочить по возрастанию два данных набора из трех чисел
# (A1, B1, C1) и (A2, B2, C2).


def SortInc3(A, B, C):
    if A > B:
        A, B = B,A
    if B > C:
        B, C = C, B
        if A > B:
          A, B = B, A
    return A, B, C


a1 = float(input('Введите первое число: '))            # Первый набор
b1 = float(input('Введите второе число: '))
c1 = float(input('Введите третье число: '))
orderly1 = SortInc3(a1, b1, c1)
print('Числа по возрастанию:', orderly1)

a2 = float(input('Введите первое число: '))            # Второй набор
b2 = float(input('Введите второе число: '))
c2 = float(input('Введите третье число: '))
orderly2 = SortInc3(a2, b2, c2)
print('Числа по возрастанию:', orderly2)