from tkinter import Tk, Frame, BOTH, Label, Entry
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import BooleanVar, Label, Entry, Checkbutton, Button, Tk, StringVar
import os
from work_window import ListFrame, Card


CURRENT_DIRECTORY = os.path.dirname(__file__)
CARDS_TYPES = ('Постоянный', 'Временный')
 
class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='gray')   
        self.parent = parent
        self.configurate_window()
        self.create_fields()
        # Фрейм с готовыми сотрудникми
        self.create_frame_with_cards()

    def configurate_window(self):
        self.parent.title('Создание пропусков сотрудников')
        self.parent.geometry('800x800+300+300')
        self.parent.iconbitmap('logo.ico')
    
    def create_fields(self, surname=None):
        Label(self.parent, text='Фамилия').grid(column=0, row=0)
        self.surname = Entry(self.parent, width=40).grid(columnspan=2, row=1)
        if surname:
            self.surname.insert(0, surname)

        # Имя
        Label(self.parent, text='Имя').grid(column=0, row=2)
        self.name = Entry(self.parent).grid(column=0, row=3)

        # Отчество
        Label(self.parent, text='Отчество').grid(column=1, row=2)
        self.midlename = Entry(self.parent).grid(column=1, row=3)

        # Компания
        Label(self.parent, text='Компания').grid(column=0, row=4)
        self.company = Entry(self.parent).grid(column=0, row=5)

        # Должность
        Label(self.parent, text='Должность').grid(column=0, row=6)
        self.midlename = Entry(self.parent).grid(column=0, row=7)

        # Просто текст
        Label(self.parent, text='Тип пропуска').grid(column=0, row=8)
        self.card_type = Combobox(self.parent)
        self.card_type.grid(column=0, row=7) 
        self.card_type['values'] = CARDS_TYPES
        # Предустановленное значение поля
        # self.card_type.current(0)
        """ 
        Чтобы получить элемент select, вы можете использовать функцию get
        вот таким образом: combo.get()
        """

        # ПЕРЕДЕЛАТЬ. НУЛИ И ДЕИНИЦЫ НЕ ПРАВИЛЬНО РАБОТАЮТ
        self.access = 0
        self.access = Checkbutton(self.parent, text='Выбрать', var=self.access, command = self.on_check)
        self.access.grid(column=0, row=9)

        # Загрузка файла
        btn = Button(self.parent, text='Загрузите фотографию', command=self.load_photo)
        btn.grid(column=0, row=9)

        # Добавление сотрудника в список
        btn = Button(self.parent, text='Добавить', command=self.create_card)
        btn.grid(column=0, row=10)

        # Закончить создание
        btn = Button(self.parent, text='Сгенерировать', command=self.pdf_creater)
        btn.grid(column=0, row=11)

        # Удалить одного из готовых
        btn = Button(self.parent, text='Удалить', command=self.delete_user)
        btn.grid(column=0, row=12)

        # Удалить одного из готовых
        btn = Button(self.parent, text='Изменить', command=self.patch)
        btn.grid(column=0, row=13)

    def create_frame_with_cards(self):
        self.users = []
        self.frame = ListFrame(self.parent, self.users)
        self.frame.grid(column=0, row=14)


    def create_card(self):
        card = Card(
            self.surname.get(),
            self.name.get(),
            self.midlename.get(),
            self.card_type.get(),
            self.access
        )
        print(card)
        value = str(self.surname.get())
        if value:
            self.frame.insert_item(value)

    def on_check(self):
        if self.access == 0:
            self.access = 1
        else:
            self.access = 0

    def load_photo(self):
        filedialog.askopenfilename(initialdir=CURRENT_DIRECTORY + r'\photo')
    
    def patch(self):
        patch_card = self.frame.curselection()
        self.set_fields(surname=patch_card)
    
    def delete_user(self):
        return self.frame.pop_selection()

    # Функция, которая будет создавать pdf файл
    def pdf_creater(self):
        if self.frame.is_empty():
            message = 'Сначала сделай работу!'
        else:
             message = 'Можешь пойти покушать'
        return messagebox.showinfo(title='Ты справился!', message=message)

def main():
    root = Tk()
    app = Application(root)
    root.mainloop()  


if __name__ == '__main__':
    main()