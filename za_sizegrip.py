import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Sizegrip Demo')
root.geometry('300x200')
root.resizable(True, True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=1, sticky=tk.SE)

root.mainloop()
