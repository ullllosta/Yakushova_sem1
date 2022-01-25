# Из предложенного текстовго файла (text18-31.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв.
# Сформировать новый файл, в который поместить строку наименьшей длины.
print(open('text18-31.txt').read(), '\n' + str(len([i for i in open('text18-31.txt').read() if i.isalpha()])))
print(min(open('text18-31.txt').readlines()), file=open('new_file18_31.txt', 'w'))