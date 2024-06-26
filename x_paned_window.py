import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('PanedWindow Demo')
root.geometry('300x200')

style= ttk.Style()
style.theme_use('classic')

pw = ttk.Panedwindow(orient=tk.HORIZONTAL)

left_list = tk.Listbox(root)
left_list.pack(side=tk.LEFT)
pw.add(left_list)

right_list = tk.Listbox(root)
right_list.pack(side=tk.LEFT)
pw.add(right_list)

pw.pack(fill=tk.BOTH, expand=True)

root.mainloop()
