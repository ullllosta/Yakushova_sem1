# Из заданной строки отобразить только символы нижнего регистра.
# Использовать библиотеку string. Строка 'In PyCharm, you can specify
# third-party stan alone application and run them as External Tools.'


from string import ascii_lowercase
line_1 = 'In PyCharm, you can specify third-party stan alone application and run them as External Tools.'
print(list(n for n in line_1 if n in ascii_lowercase))