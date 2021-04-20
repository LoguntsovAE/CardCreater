from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog
from os import path

CARDS_TYPES = ('Постоянный', 'Временный', 'Машинка')

def find_screen_center():
    """ Можно высчитывать размер экрана
    и распологать окно в его центр"""
    pass


# Функция, которая будет создавать pdf файл
def pdf_creater():
    # res = messagebox.askquestion('Заголовок1', 'Текст')
    # res = messagebox.askyesno('Заголовок2', 'Текст')
    # res = messagebox.askyesnocancel('Заголовок3', 'Текст')
    # res = messagebox.askokcancel('Заголовок4', 'Текст')
    # res = messagebox.askretrycancel('Заголовок5', 'Текст')
    pass


def load_photo():
    cur_dir = path.dirname(__file__)
    filedialog.askopenfilename(initialdir=cur_dir + '\work')


def create_work_window():
    window = Tk()
    window.title('Добро пожаловать, Администратор!')

    # устанавливается размер и положение окна
    window.geometry('600x800+500+500')

    # Просто текст
    lbl = Label(window, text="Фамилия")
    # state = active - можно установить состояние поля
    lbl.grid(column=0, row=0)
    # Устаналиваем поле ввода
    txt = Entry(window,width=10)  
    txt.grid(column=0, row=1)
    
    # Просто текст
    lbl = Label(window, text="Имя")
    lbl.grid(column=1, row=0)
    # Устаналиваем поле ввода
    txt = Entry(window,width=10)  
    txt.grid(column=1, row=1)

    # Просто текст
    lbl = Label(window, text="Отчество")
    lbl.grid(column=2, row=0)
    # Устаналиваем поле ввода
    txt = Entry(window,width=10)  
    txt.grid(column=2, row=1)

    # Просто текст
    lbl = Label(window, text="Тип пропуска")
    lbl.grid(column=3, row=0)
    # Устаналиваем поле ввода
    combo = Combobox(window)
    combo.grid(column=3, row=1) 
    combo['values'] = CARDS_TYPES
    combo.current(0)
    """ 
    Чтобы получить элемент select, вы можете использовать функцию get
    вот таким образом: combo.get()
    """
    chk_state = BooleanVar()  
    chk_state.set(False)  # задайте проверку состояния чекбокса (по умолчанию так)
    chk = Checkbutton(window, text='Доступ на грузовой двор', var=chk_state)
    chk.grid(column=3, row=2)

    # Загрузка файла
    btn = Button(window, text="Загрузите фотографию!", command=load_photo)
    btn.grid(column=4, row=1)

    # Устанавливаем кнопку
    if chk_state == True:
        btn = Button(window, text="С доступом!", command=pdf_creater)
    else:
        btn = Button(window, text="Без!", command=pdf_creater)
    btn.grid(column=0, row=6)

     

    window.mainloop()