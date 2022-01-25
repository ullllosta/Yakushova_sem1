# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы первой трети:
# Минимальный элемент первой трети:

from random import randint

i = 0    # генерация списка
f1 = []
while i < 12:
    f1.append(str(randint(-15, 0)))
    i += 1
print(f1)
print(",".join(f1), file=open('file1.txt', 'w'))  # помещение данных списка в файл

i = 0   # генерация списка
f2 = []
while i < 12:
    f2.append(str(randint(0, 15)))
    i += 1
print(f2)
print(",".join(f2), file=open('file2.txt', 'w'))  # помещение данных списка в файл

# задание1
f3 = open('data.txt', 'w', encoding='utf-8')
f3.write('Исходные данные первого файла: ')
f3.writelines(f1)
f3.write('\n')
f3.close()

f3 = open('data.txt', 'a', encoding='utf-8')
f3.write('Исходные данные второго файла: ')
f3.writelines(f2)
f3.write('\n')
f3.close()


# задание2
elem1 = int(len(f1))
elem2 = int(len(f2))
k = str(elem2 + elem1)
f3 = open('data.txt', 'a', encoding='utf-8')
f3.write('Количество элементов первого и второго файлов: ')
f3.writelines(k)
f3.write('\n')
f3.close()

# задание3
f3 = open('data.txt', 'a', encoding='utf-8')
f3.write('Первая треть элементов первого файла: ')
f3.writelines(f1[:4])
f3.write('\n')
f3.close()

f3 = open('data.txt', 'a', encoding='utf-8')
f3.write('Первая треть элементов второго файла: ')
f3.writelines(f2[:4])
f3.write('\n')
f3.close()

# задание4
f3 = open('data.txt', 'a', encoding='utf-8')
f3.write('Наименьший элемент первого файла: ')
f3.writelines(min(f1[:4]))
f3.write('\n')
f3.close()

f3 = open('data.txt', 'a', encoding='utf-8')
f3.write('Наименьший элемент второго файла: ')
f3.writelines(min(f2[:4]))
f3.write('\n')
f3.close()