import tkinter as tk


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


class Card():
    def __init__(self, surname, name, midlename, card_type, chk_state):
        self.surname = surname
        self.name = name
        self.midlename = midlename
        self.card_type = card_type
        self.chk_state = chk_state

    def __str__(self):
        return  self.surname + ' ' + self.name + ' ' + self.midlename + ' ' + self.card_type + ' Тип: ' + str(self.chk_state)

    # def method(self):
    #     return value

