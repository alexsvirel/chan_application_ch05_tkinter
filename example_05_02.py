# ! /usr/Ьin/env python
"""
Вместо метки ставим кнопку, Hello World!

Создаем окно верхнего уровня.
Добавляем графический элемент Button, который содержит строку Hello World! и один
дополнительный параметр, метод Tkinter.quit(). Эrот метод устанавливает обратный вызов
к кнопке, чтобы после ее нажатия (и отпускания) завершалось все приложение.
"""
from tkinter import *

top = Tk()
quit = Button(top, text='Hello World!', command=top.quit)
quit.pack()
top.mainloop()
