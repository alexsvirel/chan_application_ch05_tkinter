# ! /usr/Ьin/env python
"""
К текстовой метке и кнопке добавляем ползунок Scale

Создаем окно верхнего уровня и добавляем графические элементы Label, Button и Scale.

Графический элемент Scale используется для взаимодейсrвия с графическим элементом LaЬel.
Он определяет ползунок - инструмент, который управляет размером текстовоrо шрифта
в графическом элементе LaЬel.
Чем выше расположен ползунок, тем крупнее шрифт, и наоборот.
"""
from tkinter import *


def resize(ev=None):
    """
    изменяет размер шрифта метки label при перемещении ползунка scale
    """
    label.config(font='Helvetica -%d bold' % scale.get())


top = Tk()
top.geometry('250x150')                 # задан размер окна при открытии

label = Label(top, text='Hello World', font='Helvetica -12 bold')
label.pack(fill=Y, expand=YES)

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=YES)

quit = Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quit.pack()

mainloop()
