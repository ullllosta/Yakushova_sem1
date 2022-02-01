# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу.
# https://mob25.com/images/Perl/images/ris150_1.jpg

from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import scrolledtext

window = Tk()
window.title('Регистрация')
window.geometry('726x528')
Label(text='Регистрационная страница Клуба любителей фантастики', width=65, height=3, font='arial 16').place(x=-50, y=-10)
Label(text='Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой.', width=80, font='arial 11').place(x=-85, y=60)
Label(text='Введите регистрационное имя:', width=28, font='arial 11').place(x=-11, y=105)
Entry(width=19, font='arial 11').place(x=250, y=108)
Label(text='Введите пароль:', width=28, font='arial 11').place(x=-61, y=130)
Entry(width=19, font='arial 11').place(x=250, y=133)
Label(text='Подтвердите пароль:', width=28, font='arial 11').place(x=-45, y=155)
Entry(width=19, font='arial 11').place(x=250, y=158)
Label(text='Ваш возраст:', width=28, font='arial 11').place(x=-71, y=195)
selected = IntVar()
Radiobutton(window, text='До 20', value=0, variable=selected).place(x=110, y=196)
Radiobutton(window, text='20-30', value=1, variable=selected).place(x=180, y=196)
Radiobutton(window, text='30-50', value=2, variable=selected).place(x=250, y=196)
Radiobutton(window, text='Старше 50', value=3, variable=selected).place(x=320, y=196)
Label(text='На каких языках читаете:', width=28, font='arial 11').place(x=-30, y=238)
chk = BooleanVar()
chk.set(True)
Checkbutton(window, text='русский', variable=chk).place(x=190, y=240)
chk1 = BooleanVar()
chk1.set(False)
Checkbutton(window, text='английский', variable=chk1).place(x=260, y=240)
chk2 = BooleanVar()
chk2.set(False)
Checkbutton(window, text='французский', variable=chk2).place(x=350, y=240)
chk3 = BooleanVar()
chk3.set(False)
Checkbutton(window, text='немецкий', variable=chk3).place(x=445, y=240)
Label(text='Какой формат данных является для Вас предпочтительным', width=50, font='arial 11').place(x=-9, y=280)
format1 = Listbox(height=2, width=12)
list1 = ["HTML", "Plain text"]
for i in list1:
    format1.insert(END, i)
format1.place(x=11, y=303)
Label(text='Ваши любимые авторы:', width=30, font='arial 11').place(x=-44, y=367)
scrolledtext.ScrolledText(window, width=45, height=3).place(x=14, y=390)
Button(text="Ок").place(x=14, y=460)
Button(text="Отменить").place(x=44, y=460)
Scrollbar().pack(side=RIGHT, fill=Y)
window.mainloop()
