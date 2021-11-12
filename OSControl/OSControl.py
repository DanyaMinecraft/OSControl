import threading
import time
import tkinter.messagebox
from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox

import Info.Information


def clock_update():  # Часы
    while True:
        lbl_time['text'] = (datetime.utcnow() + timedelta(hours=3)).strftime('Сейчас: %d.%m.%g %H:%M:%S')
        time.sleep(0.5)


def Open():  # Открытие меню О программе
    window.withdraw()
    About_Program = Tk()
    About_Program.title("OSControl {0}".format(Info.Information.version))  # импорт переменной version
    About_Program.geometry("720x480")


def Start():  # Кнопка запуска меню программы
    window.withdraw()
    menu = Tk()
    menu.title("OSControl {0}".format(Info.Information.version))  # импорт переменной version из файла информации
    menu.geometry("720x480")


def Quit(tk=None):
    if messagebox.askokcancel("Выход!", "Вы уверены что хотите выйти из программы?"):
        quit()


window = Tk()
window.title("OSControl {0}".format(Info.Information.version))
Function1 = Label(window, text="Добро пожаловать в OSControl", padx="35", pady="120", font=("Arial Black", 30))
Function1.grid()
window.geometry("720x480")
lbl_time = Label()
lbl_time.place(relx=0, rely=1, anchor="sw", bordermode=OUTSIDE)
process = threading.Thread(target=clock_update)
process.start()
Quit = Button(window, text="Выход", command=Quit, font=("Arial Black", 15))
Quit.grid()
OpenMenu = Button(window, text="Начать", command=Start, font=("ArialBlack", 15))
OpenMenu.grid()
About = Button(window, text="О программе", command=Open, font=("Arial Black", 15))
About.grid()
window.mainloop()
