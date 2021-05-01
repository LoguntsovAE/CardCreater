import tkinter as tk
import os
from PIL import Image


CURRENT_DIRECTORY = os.path.dirname(__file__)


class ListFrame(tk.Frame):
    def __init__(self, master, items=[]):
        super().__init__(master)
        self.list = tk.Listbox(self)
        self.scroll = tk.Scrollbar(self, orient=tk.VERTICAL,
                                   command=self.list.yview)
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.insert(0, *items)
        self.list.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)

    def curselection(self):
        index = self.list.curselection()
        if index:
            value = self.list.get(index)
            return value

    def pop_selection(self):
        index = self.list.curselection()
        if index:
            value = self.list.get(index)
            self.list.delete(index)
            return value

    def insert_item(self, item):
        self.list.insert(tk.END, item)

    def is_empty(self):
        return len(self.list.get(0)) == 0


class Card:
    def __init__(self, surname, name,
        midlename, company, position, card_type, access, date, number, photo
    ):
        self.surname = surname
        self.name = name
        self.midlename = midlename
        self.company = company
        self.position = position
        self.card_type = card_type
        self.access = access
        self.date = date
        self.number = number
        self.photo = photo
        
        # Вызовем метод создания картинки
        self.create_card_image()


    def __str__(self):
        return  self.surname + ' ' + self.name + ' ' + self.midlename + ' ' + self.card_type + ' Тип: ' + str(self.chk_state)

    def show(self):
        root = tk.Tk()        
        label = tk.Label(root, text=self.surname)
        # label.image = photo
        label.pack()
        root.mainloop()

    def create_card_image(self):
        temp = Image.open(r'template\template_main.png')
        image_labe = self.photo.paste(temp)
        root = tk.Tk()        
        label = tk.Label(root, image=image_labe)
        label.image = image_labe
        label.pack()
        root.mainloop()

        temp.close()
