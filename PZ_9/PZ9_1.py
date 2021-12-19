# В магазинах имеются следующие товары.
# Магнит – молоко, соль, сахар.
# Пятерочка – мясо, молоко, сыр.
# Перекресток – молоко, творог, сыр, сахар. Определить:
# 1)В каких магазинах нельзя приобрести сыр.
# 2)В каких магазинах можно приобрести одновременно молоко и сахар.
# 3)В каких магазинах можно приобрести соль.

magnit = {'молоко', 'соль', 'сахар'}
pyaterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}
a = set()


# 1
for i in magnit, pyaterochka, perekrestok:
    if not 'сыр' in magnit:
        a.add('магнит')
    if not 'сыр' in pyaterochka:
        a.add('пятерочка')
    if not 'сыр' in perekrestok:
        a.add('перекресток')
print('Сыр нельзя преобрести в магазинах: ', a), a.clear()


# 2
for i in magnit, pyaterochka, perekrestok:
    if 'молоко' and 'сахар' in magnit:
        a.add('магнит')
    if 'молоко' and 'сахар' in pyaterochka:
        a.add('пятерочка')
    if 'молоко' and 'сахар' in perekrestok:
        a.add('перекресток')
print('Молоко и сахар можно преобрести в магазинах: ', a), a.clear()


# 3
for i in magnit, pyaterochka, perekrestok:
    if 'соль' in magnit:
        a.add('магнит')
    if 'соль' in pyaterochka:
        a.add('пятерочка')
    if 'соль' in perekrestok:
        a.add('перекресток')
print('соль можно преобрести в магазинах: ', a)