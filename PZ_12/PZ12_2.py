# Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника.
# Проверить истинность высказывания: «Треугольник со сторонами a, b, c является равнобедренным».

from tkinter import*

def obrabotka(event):
    a = int(num1.get())
    b = int(num2.get())
    c = int(num3.get())

    if a == b or b == c or a == c:
        t = 'Треугольник равнобедренный!'
    else:
        t = 'Треугольник неравнобедренный!'

    otvet['text'] = f"Ответ: {t}"

window = Tk()
window.title("Проверка истиности высказывания")
window.geometry("350x233+233+233")


Label(text="Сторона a").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

Label(text="Сторона b").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

Label(text="Сторона c").grid(row=3, column=0)
num3 = Entry()
num3.grid(row=3, column=1)

button1 = Button(text="Проверить")
button1.place(x=200, y=20)
otvet = Label()
otvet.place(x=0, y=70)

button1.bind('<Button-1>',obrabotka)


window.mainloop()