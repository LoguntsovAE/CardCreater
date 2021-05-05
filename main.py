from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
from datetime import date, timedelta
from work_window import Card
import os
from main_window_settings import main_window_settings


CURRENT_DATE = date.today()
FUTURE_DATE = (date.today() + timedelta(days=11)).strftime('%d.%m.%Y')
CURRENT_DIRECTORY = os.path.dirname(__file__)
CARDS_TYPES = ('Постоянный', 'Временный')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Объявляем пустой список с готовыми карточками
        self.cards = []

        self.frame_fields = tk.Frame(master=master, relief=tk.SUNKEN, borderwidth=5, background='gray')
        self.frame_fields.pack()
        main_title_1 = tk.Label(master=self.frame_fields, text='Создание карты сотрудника', background='gray')
        main_title_1.pack(side=tk.TOP)
        self.create_widgets_fields(frame=self.frame_fields)

        self.frame_cards = tk.Frame(relief=tk.GROOVE, borderwidth=5, background='blue')
        self.frame_cards.pack()
        main_title_2 = tk.Label(master=self.frame_cards, text='Просмотр и редактирование')
        main_title_2.pack(side=tk.TOP)
        self.create_widgets(self.frame_cards)


    def create_widgets_fields(self, frame,
        surname=None, name=None, midlename=None,
        company=None, position=None, card_type=None,
        date=None, special_access=None, number=None):
        
        ### SURNAME
        srn = tk.Label(master=self.frame_fields, text='Фамилия', background='white')
        srn.pack()
        self.surname = tk.Entry(self.frame_fields, width=40)
        self.surname.pack()
        if surname is not None:
            self.surname.insert(0, surname)
        ###

        ### NAME
        nme = tk.Label(master=self.frame_fields, text='Имя', background='white')
        nme.pack()
        self.name = tk.Entry(self.frame_fields, width=40)
        self.name.pack()
        if name is not None:
            self.name.insert(0, name)
        ###

        ### MIDLENAME
        midnme = tk.Label(master=self.frame_fields, text='Имя', background='white')
        midnme.pack()
        self.midlename = tk.Entry(self.frame_fields, width=40)
        self.midlename.pack()
        if midlename is not None:
            self.midlename.insert(0, midlename)
        ###

        ### COMPANY
        cmp = tk.Label(master=self.frame_fields, text='Компания', background='white')
        cmp.pack()
        self.company = tk.Entry(self.frame_fields, width=40)
        self.company.pack()
        if company is not None:
            self.company.insert(0, company)
        ###

        ### POSITON
        pst = tk.Label(master=self.frame_fields, text='Должность', background='white')
        pst.pack()
        self.position = tk.Entry(self.frame_fields, width=40)
        self.position.pack()
        if position is not None:
            self.position.insert(0, position)
        ###

        ### CARD_TYPE
        ct = tk.Label(master=self.frame_fields, text='Тип пропуска', background='white')
        ct.pack()
        self.card_type = tk.ttk.Combobox(self.frame_fields)
        self.card_type.pack()
        self.card_type['values'] = CARDS_TYPES
        if card_type is not None:
            self.card_type.insert(0, card_type)
        ###

        ### SPECIAL_ACCESS
        access = tk.Checkbutton(self.frame_fields, text='Доступ на грузовой двор', command = self.on_check)
        if special_access is not None:
            self.access = special_access
        else:
            self.access = 0
        access.pack()
        ###

        ### FINISH_DAY
        fd = tk.Label(master=self.frame_fields, text='Дата окончания', background='white')
        fd.pack()
        self.date = DateEntry(master=self.frame_fields, background='darkblue',
        foreground='white', borderwidth=2, textvariable='12.12.12'
        )
        self.date.set_date(FUTURE_DATE)
        self.date.pack()
        ###

        ### NUMBER
        ct = tk.Label(master=self.frame_fields, text='Номер', background='white')
        ct.pack()
        self.number = tk.Entry(self.frame_fields, width=40)
        self.number.pack()
        if number is not None:
            self.number.insert(0, number)
        ###

        ### PHOTO
        picture = tk.Label(master=self.frame_fields, text="Добавить фото", image=None, width=12, height=9, borderwidth=1, relief="groove")
        picture.bind('<Double-Button-1>', lambda event: self.open_img(event, picture))
        picture.pack()
        ###
        
        btn = tk.Button(
            self.frame_fields,
            text='Создать',
            # Здесь нужно перехватить исключение вызова функции
            command = lambda: self.create_card(
                    surname=self.surname.get(),
                    name=self.name.get(),
                    midlename=self.midlename.get(),
                    company=self.company.get(),
                    position=self.position.get(),
                    card_type=self.card_type.get(),
                    access=self.access,
                    date=self.date.get(),
                    number=self.number.get(),
                    photo=self.photo,
                )
        )
        btn.pack()


    def on_check(self):
        if self.access == 1:
            self.access = 0
        else:
            self.access = 1
        return self.access


    def open_img(self, event, picture):
        try:
            self.file_name = filedialog.askopenfilename(
                initialdir=CURRENT_DIRECTORY + r'\photo',
                title='Выбирете фотографию сотрудника',
                filetypes=(('JPG File', '*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*'))
            )
            img = Image.open(self.file_name)
            img.thumbnail((81,108))
            # img = img.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            picture.configure(image=photo, width=81, height=108, background='red')
            picture.image = self.photo = photo
        except Exception as e:
            print(e)
            messagebox.showerror('Ошибка загрузки', 'Картинка не загрузилась :(')
        try:
            file_name = os.path.basename(self.file_name).split()
            if self.surname.get() == '':
                self.surname.insert(0, file_name[0])
            if self.name.get() == '':
                self.name.insert(0, file_name[1])
            # Список слов, которые должны быть удалены из автовставки
            for_deliting = ['.jpg']
            midlename = file_name[2]
            for word in for_deliting:
                midlename = midlename.replace(word, '')
            self.midlename.insert(0, midlename)
        except Exception as e:
            print(e)
            messagebox.showerror('Ошибка автозаполнения', 'Введите ФИО ручками')
        

    def create_card(self, surname, name, midlename, company, position, card_type, access, date, number, photo):
        try:
            card = Card(surname, name, midlename, company, position, card_type, access, date, number, photo)
            self.card.append(card)
            # self.surname = surname
            # self.name = name
            # self.midlename = midlename
            # self.company = company
            # self.position = position
            # self.card_type = card_type
            # self.access = access
            # self.date = date
            # self.number = number
            # self.photo = photo
        except Exception as e:
            print(e)
            messagebox.showerror('Ошибка создания', 'Неудалось создать карточку. Начните сначала')
        # хотел сделать предпросмотр, пока не получается
        # card.show()

    def create_widgets(self, frame):
        main_title_1 = tk.Label(master=self.frame_fields, text=self.cards, background='gray')
        main_title_1.pack()


if __name__ == '__main__':
    root = tk.Tk()
    main_window_settings(root)
    app = Application(root)
    root.mainloop()