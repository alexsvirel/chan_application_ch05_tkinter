#!/usr/bin/env python3
""" Проrрамма для навиrации по файловой системе

Графический пользовательский интерфейс стал немного сложнее в
результате применения графических элементов, добавления окон со списками, полей
ввода текста и линеек прокрутки к прежнему набору. Увеличилось также разнообразие
функций обратного вызова, которые теперь позволяют реагировать на щелчки
кнопкам и мыши, нажатия клавиш и действия с линейкой прокрутки."""
# первые несколько строк включают обычную строку запуска Unix, операторы
# импорта модуля os, метода t ime . s leep ( ) и всех атрибутов модуля Tkinter.
import os
from time import sleep
from tkinter import *


# В строках 17 - определен конструктор для класса DirList - объекта, который
# представляет рассматриваемое приложение. Первый создаваемый объект Label содержит
# метку с главным заголовком приложения и номером версии.
class DirList(object):

    def __init__(self, initdir=None):
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()
        # В объявлении переменной Tk с именем cwd задается имя текущего каталога; эта
        # переменная потребуется в дальнейшем.
        self.cwd = StringVar(self.top)
        # Следующий создаваем ый объект Label служит для отображения имени текущею каталога.
        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()
        # В этом разделе определяется основная часть применяемого rрафического пользовательского
        # интерфейса, объект Listbox с именем dirs, который содержит листинг
        # файлов рассматриваемого каталога. Применяется объект Scrollbar, позволяющий
        # пользователю прокручивать листинг, если количество файлов превышает размер
        # объекта Listbox по вертикали. Оба этих графических элемента содержатся в rрафическом
        # элементе Frame. Элементы Listbox и меют обратный вызов (setDi rAndGo),
        # привязанный к ним с использованием метода Ьind ( ) Listbox.
        # Под привязкой подразумевается установление соответствия между нажатием клавиши,
        # действием мышью или каким-то другим событием и обратным вызовом, который
        # выполняется при формировании такого события пользователем. Вызов функции
        # setDirAndGo ( ) происходит после двойного щелчка на одном из элементов в списке
        # Listbox. Привязка элемента Scrollbar к элементу Listbox осуществляется путем
        # вызова метода Scrollbar . config ( ) .
        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind("<Double-1>", self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()
        # Затем создается поле ввода Entry, в котором пользователь может ввести имя каталога,
        # в который требуется перейти и просмотреть содержащиеся в нем файлы с
        # помощью элемента L i s tbox. К этому полю ввода добавлена привязка к клавише
        # <Enter>, чтобы пользователь мог нажимать эту клавишу возврата вместо щелчка
        # кнопкой. Эго относится и к привязке м ыши, которая рассматривалась ранее, применительно
        # к элементу Listbox. После того как пользователь дважды щелкнет на элементе
        # в списке Li s tbox, осуществляется такое же действие, как при вводе имени каталога
        # вручную в поле ввода Entry с последующим щелчком на кнопке Go (Перейти).
        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind("<Return>", self.doLS)
        self.dirn.pack()
        # Затем определяется рамка Button (Ьfm) для размещения в ней трех кнопок: кнопки
        # "очистки" (clr), кнопки "перехода" (ls) и кнопки "завершения" (quit). С каждой
        # кнопкой связаны собственная конфиrурация и обратный вызов, активизируемый после
        # щелчка на ней.
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
                          activeforeground='white', activebackground='blue')
        self.ls = Button(self.bfm, text="List Directory", command=self.doLS,
                         activeforeground='white', activebackground='green')
        self.quit = Button(self.bfm, text="Quit", command=self.top.quit,
                           activeforeground='white', activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()
        # В последней части конструктора инициализируется программа графического
        # пользовательского интерфейса, действие которой начинается с текущего рабочего каталога.
        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    # Метод cclrDir() очищает строковую переменную Tk с именем cwd, которая содержит
    # имя текущего активного каталога. Эга переменная используется для отслеживания
    # того, какой каталог рассматривается в данный момент, и, что более важно,
    # помогает отслеживать предыдущий каталог на случай, если возникнут ошибки. Интерес
    # представляют также переменные ev в функциях обратного вызова, имеющие
    # значение по умолчанию None. Каждое из таких значений может быть передано по
    # назначению с помощью системы управления окнами. Значения этих переменных в
    # случае необходимости могут использоваться в функциях обратного вызова.
    def clrDir(self, ev=None):
        self.cwd.set('')

    # Метод setDirAndGo ( ) задает каталог, в котором необходимо получить листинг
    # файлов, и формирует вызов метода, с помощью которого осуществляется это действие,
    # doLS ( ) .
    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    # Метод doLS ( ) , безусловно, является наиболее важным с точки зрения организации
    # работы всего этого приложения с графическим пользовательским интерфейсом.
    # В нем выполняются все предохранительные проверки (например, содержит ли текстовая
    # строка имя каталога и существует ли этот каталог). Если возникает какая-либо
    # ошибка, то в качестве текущего каталога снова устанавливается последний каталог.
    # Если же ошибка не обнаруживается, то происходит вызов метода os . listdir ( ) для
    # получения фактических данных о файлах, присутствующих в каталоге, и с помощью
    # этих данных происходит замена листинга в элементе Listbox. В то время как в фоновом
    # режиме продолжается работа по выборке информации из нового каталога, синяя
    # полоса, выделенная подсветкой, становится ярко красной. После окончательного
    # перехода в новый каталог восстанавливается синий цвет полосы.
    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir: tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return

        self.cwd.set("FETCHING DIRECTORY CONTENTS...")
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground="LightSkyBlue")


# Функция rnain ( ) выполняется только в случае непосредственного вызова
# сценария; после запуска rnain ( ) на выполнение разворачивается приложение с графическим
# пользовательским интерфейсом, а затем вьвывается функция rnainloop ( )
# для запуска графического пользовательского интерфейса, которому передается контроль
# над приложением.
def main():
    d = DirList(os.curdir)
    mainloop()


if __name__ == "__main__":
    main()
