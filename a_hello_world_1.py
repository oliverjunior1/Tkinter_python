import tkinter as tk

root = tk.Tk()

message = tk.Label(root, text='Hello, World')
message.pack()
root.geometry('500x500')

root.mainloop()