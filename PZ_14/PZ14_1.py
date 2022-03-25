# Из исходного текстового файла (price.txt) выбрать все цены.
# Посчитать количество полученных элементов.
import re
with open('price.txt', 'r') as file:
    text = file.read()
    price2 = re.findall("\d+\sруб\.\s\d+\sкоп", text)
    print(price2)
    print(len(price2))