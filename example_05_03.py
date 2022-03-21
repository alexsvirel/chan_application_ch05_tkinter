# ! /usr/Ьin/env python
"""
Ставим и текстовую метку и кнопку

Создаем окно верхнего уровня.
создаtv два графических элемента, Label и Button.
Кнопке задаем дополнительные параметры:
bg='red' (цвет текста),
fg='white' цвет фона кнопки)
fill='x' (кнопка растягивается по горизонтали),
expand='YES' (кнопка заполняет все отведенное ей пространство)
"""
from tkinter import *

top = Tk()

hello = Label(top, text='Hello World!')
hello.pack()

quit = Button(top, text='Quit', command=top.quit, bg='red', fg='white')
quit.pack(fill=X, expand=YES)

top.mainloop()
