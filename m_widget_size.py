# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.title('Tkinter Widget Size')
# root.geometry('600x400')
#
# label1 = tk.Label(master=root, text='Sizing', bg='red', fg='white', width=8, font=('Helvetica', 24))
#
# label1.pack()
#
# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Widget Size')
root.geometry('600x400')

label1 = tk.Label(master=root, text='Sizing', bg='red', fg='white', width=20)
label1.pack(fill=tk.X)

root.mainloop()
