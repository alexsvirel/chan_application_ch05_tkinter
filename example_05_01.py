# ! /usr/Ьin/env python
"""
Передаем привет всему миру, Hello World! https://github.com/schedutron/CPAP

Создаем окно верхнего уровня.
Добавляем графический элемент LaЬel, который содержит строку Hello World!.
Диспетчер окон Packer получает указание взять на себя управление этим графическим элементом
и отобразить его, а затем следует вызов функции mainloop() и начинается выполнение
приложения с графическим пользовательским интерфейсом.
"""
from tkinter import *

top = Tk()
label = Label(top, text='Hello World!')
label.pack()
top.mainloop()
