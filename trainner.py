from tkinter import *
from tkinter import ttk

root = Tk()
def change():
    label.config(text='Jesus is the way', fg='red', bg='yellow')

label = Label(root, text='Press to see a message:')
button = Button(root, text='Press', command=change)
label.pack()
button.pack()

root.geometry('500x500')

root.mainloop()
