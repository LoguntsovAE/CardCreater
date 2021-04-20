from tkinter import *


def find_screen_center():
    """ Можно высчитывать размер экрана
    и распологать окно в его центр"""
    pass


# Функция, которая будет создавать pdf файл
def pdf_creater(lbl):
    lbl.configure(text="Я же просил...")


def create_work_window():
    window = Tk()
    window.title('Добро пожаловать, Администратор!')

    # устанавливается размер и положение окна
    window.geometry('400x600+500+500')
    lbl = Label(window, text="Привет")
    lbl.grid(column=0, row=0)
    
    # Устанавливаем кнопку
    btn = Button(window, text="Не нажимать!", command=pdf_creater(lbl))
    btn.grid(column=0, row=1)

    window.mainloop()