from PIL import Image, ImageTk
from tkinter import Tk, Frame, BOTH, Label, Entry
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import BooleanVar, Label, Entry, Checkbutton, Button, Tk, StringVar, Canvas
import os
from work_window import ListFrame, Card
from tkcalendar import Calendar
from datetime import date
from tkinter import PhotoImage

CURRENT_DATE = date.today().strftime('%d.%m.%Y')
CURRENT_DIRECTORY = os.path.dirname(__file__)
CARDS_TYPES = ('Постоянный', 'Временный')



class Application(Frame):
    def __init__(self, parent):
        frame1 = Frame(parent, background='red').pack()
        frame2 = Frame().pack()
        # не удаляй фрейм
        # Frame.__init__(self, parent, background='gray')   
        self.parent = parent
        # Создаём главное окно приложения
        self.configurate_window()
        # Создаём поля для ввода данных карточки
        # self.create_fields()
        # Создаём фрейм с готовыми сотрудникми
        # self.create_frame_with_cards()
        # Загрузка файла
        # Button(self.parent, text='Добавить фото', command=self.load_photo).pack()
        # img = Image.open('D:\Dev\CardCreater\d1.jpg')
        # img = img.resize((90, 120), Image.ANTIALIAS)
        # self.photo = ImageTk.PhotoImage(img)
        # self.canvas = Canvas(self.parent, height=120, width=90, background='gray')
        # self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        # self.canvas.pack()
        # panel = Label(self.parent, image=self.photo)
        # panel.image = self.photo
        # panel.pack()
        # self.photo = None
        # load_photo_btn = Button(self.parent, text='Добавить фото', command=self.load_photo).pack()
        # load_photo_btn.bind
        # panel = Label(self.parent, image=self.photo)
        # panel.pack()

    def configurate_window(self):
        self.parent.title('Создание пропусков сотрудников')
        self.parent.geometry('800x800+300+300')
        self.parent.iconbitmap('logo.ico')
    
    def create_fields(self, surname=None):
        Label(self.parent, text='Фамилия').pack()
        self.surname = Entry(self.parent, width=40)
        self.surname.pack()
        if surname:
            self.surname.insert(0, surname)

        # Имя
        Label(self.parent, text='Имя').pack()
        self.name = Entry(self.parent)
        self.name.pack()

        # Отчество
        Label(self.parent, text='Отчество').pack()
        self.midlename = Entry(self.parent)
        self.midlename.pack()

        # Компания
        Label(self.parent, text='Компания').pack()
        self.company = Entry(self.parent, width=40)
        self.company.pack()

        # Должность
        Label(self.parent, text='Должность').pack()
        self.position = Entry(self.parent, width=40)
        self.position.pack()

        # Просто текст
        Label(self.parent, text='Тип пропуска').pack()
        self.card_type = Combobox(self.parent)
        self.card_type.pack()
        self.card_type['values'] = CARDS_TYPES
        # Предустановленное значение поля
        # self.card_type.current(0)
        """ 
        Чтобы получить элемент select, вы можете использовать функцию get
        вот таким образом: combo.get()
        """

        # Календарь
        Label(self.parent, text='Дата окончания').pack()
        self.date = Entry(justify='center')
        self.date.pack()
        self.date.insert(0, CURRENT_DATE)

        # ПЕРЕДЕЛАТЬ. НУЛИ И ДЕИНИЦЫ НЕ ПРАВИЛЬНО РАБОТАЮТ
        # Доступ на грузовой двор (галочка)
        start_value = 0
        self.access = Checkbutton(
            self.parent,
            text='Доступ на грузовой двор',
            var=start_value,
            command = self.on_check
        ).pack()

        # Кнопка выбора даты. пока кнопка :(
        # calendar_image = PhotoImage(file = CURRENT_DIRECTORY + r'\calendar.png')
        self.calendar_image = PhotoImage(file='python.png')
        btn = Button(
            self.parent,
            image=self.calendar_image,
            compound=tk.LEFT,
            command=self.show_calendar,
            relief='flat'
            # height=20,
            # width=55
        )
        btn.pack()


        # Добавление сотрудника в список
        btn = Button(self.parent, text='Создать', command=self.create_card)
        btn.pack()

        #
        # btn = Button(self.parent, text='Редактировать', command=self.patch)
        # btn.grid(column=0, row=12)

        #
        # btn = Button(self.parent, text='Предпросмотр', command=self.patch)
        # btn.grid(column=0, row=13)

        # 
        # btn = Button(self.parent, text='Удалить', command=self.delete_user)
        # btn.grid(column=0, row=14)

        # Закончить создание
        # btn = Button(self.parent, text='Экспорт в PDF', command=self.pdf_creater)
        # btn.grid(column=0, row=15)

    def show_calendar(self):
        self.cal = Calendar(
                   font="Arial 14", selectmode='day',
                   cursor="hand1", date=CURRENT_DATE)
        self.cal.pack()
        Button(text='Ок', command=self.set_date).pack()
        Button(text='Закрыть', command=self.set_date).pack()
        messagebox.showinfo('Привет', self.cal)
        
    def set_date(self):
        date = self.cal.selection_get()
        date2 = '{0:%d}.{0:%m}.{0:%Y}'.format(date)
        print(date2)

    def create_frame_with_cards(self):
        self.users = []
        self.frame = ListFrame(self.parent, self.users)
        self.frame.pack()

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
        file = filedialog.askopenfilename(
                title='open',
                initialdir=CURRENT_DIRECTORY + r'\photo'
            )
        # img = Image.open()
        # # print(img)
        # self.photo = ImageTk.PhotoImage(img)
        # return self.photo
        
    
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