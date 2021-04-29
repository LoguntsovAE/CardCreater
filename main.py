from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
from datetime import date
from work_window import ListFrame, Card
import os
from main_window_settings import main_window_settings


CURRENT_DATE = date.today().strftime('%d.%m.%Y')
CURRENT_DIRECTORY = os.path.dirname(__file__)
CARDS_TYPES = ('Постоянный', 'Временный')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.frame_fields = tk.Frame(master=master, relief=tk.SUNKEN, borderwidth=5, background='gray')
        self.frame_fields.pack()
        main_title_1 = tk.Label(master=self.frame_fields, text='Создание карты сотрудника', background='gray')
        main_title_1.pack(side=tk.TOP)
        self.create_widgets_fields(frame=self.frame_fields)

        self.frame_cards = tk.Frame(relief=tk.GROOVE, borderwidth=5, background='blue')
        self.frame_cards.pack()
        main_title_2 = tk.Label(master=self.frame_cards, text='Просмотр и редактирование')
        main_title_2.pack(side=tk.TOP)
        # self.create_widgets(self.frame_fields)


    def create_widgets_fields(self, frame,
        surname=None, name=None, midlename=None,
        company=None, position=None, card_type=None,
        date=None, special_access=None, number=None
    ):
        
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
        access = tk.Checkbutton(self.frame_fields, text='Доступ на грузовой двор')
        access['command'] = self.on_check
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
        foreground='white', borderwidth=2,
        )
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
        picture = tk.Label(master=self.frame_fields, text="Добавить фото", image=None, width=12, height=9, borderwidth=7, relief="groove")
        picture.bind('<Double-Button-1>', lambda event: self.open_img(event, picture))
        picture.pack()
        ###

        btn = tk.Button(
            self.frame_fields,
            text='Создать',
            command = lambda: self.create_card(
                self.surname.get(),
                self.name.get(),
                self.midlename.get(),
                self.company.get(),
                self.position.get(),
                self.card_type.get(),
                self.access,
                self.date.get(),
                self.number.get(),
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
            file = filedialog.askopenfilename(
                initialdir=CURRENT_DIRECTORY + r'\photo',
                title='Выбирете фотографию сотрудника',
                filetypes=(('JPG File', '*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*'))
            )
            img = Image.open(file)
            img.thumbnail((81,108))
            photo = ImageTk.PhotoImage(img)
            picture.configure(image=photo, width=81, height=108, background='red')
            picture.image = self.photo = photo
            print(self.photo)
        except:
            messagebox.showerror('Ошибка загрузки', 'Картинка не загрузилась :( ЛОШАРА!!!')
        messagebox.showerror('Ошибка загрузки', 'Картинка не загрузилась :( ЛОШАРА!!!')


    def create_card(self, surname, name, midlename, company, position, card_type, access, date, number):
        print(f'Hi {surname}\n{name}\n{midlename}\n{company}\n{position}\n{card_type}\n{access}\n{date}\n{number}')
    # , name, midlename, company, position, card_type,
    #     date, special_access, number
    #     pass

    def create_widgets(self, frame):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == '__main__':
    root = tk.Tk()
    main_window_settings(root)
    app = Application(root)
    root.mainloop()