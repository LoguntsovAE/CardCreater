from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
# root.geometry("700x600+1400+300")
# root.resizable(width=True, height=True)
CURRENT_DIRECTORY = os.path.dirname(__file__)

def open_img(event, picture):
    file = filedialog.askopenfilename(
        initialdir=CURRENT_DIRECTORY + r'\photo',
        title='Hello, title',
        filetypes=(('JPG File', '*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*'))
    )
    img = Image.open(file)
    img.thumbnail((74,96))
    photo = ImageTk.PhotoImage(img)
    picture.configure(text=None, image=photo, width=74, height=96, background='red')
    picture.image = photo
    

picture = Label(text="Добавить фото", image=None, width=30, height=40, borderwidth=7, relief="groove")
picture.bind('<Double-Button-1>', lambda event: open_img(event, picture))

picture.pack()
root.mainloop()
