# import tkinter as tk
#
# root = tk.Tk()
# root.title('Tkinter Pack Layout')
# root.geometry('600x400')
#
# label1 = tk.Label(master=root, text='Tkinter', bg='red', fg='white')
# label2 = tk.Label(master=root, text='Pack Layout', bg='green', fg='white')
# label3 = tk.Label(master=root, text='Demo', bg='blue', fg='white')
#
# label1.pack()
# label2.pack()
# label3.pack()
#
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.title('Tkinter Pack Layout')
# root.geometry('600x400')
#
# label1 = tk.Label(master=root, text='Tkinter', bg='red', fg='white')
# label2 = tk.Label(master=root, text='Pack Layout', bg='green', fg='white')
# label3 = tk.Label(master=root, text='Demo', bg='blue', fg='white')
#
# label1.pack(side=tk.BOTTOM)
# label2.pack(side=tk.BOTTOM)
# label3.pack(side=tk.BOTTOM)
#
# root.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Login')
root.geometry('350x220')

fields = {}

fields['username_label'] = ttk.Label(text='Username:')
fields['username'] = ttk.Entry()

fields['password_label'] = ttk.Label(text='Password')
fields['password'] = ttk.Entry(show='*')

for field in fields.values():
    field.pack(anchor = tk.W, padx = 10, pady=5, fill=tk.X)

ttk.Button(text='Login').pack(anchor=tk.W, padx=10, pady=5)

root.mainloop()