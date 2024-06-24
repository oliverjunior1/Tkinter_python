import tkinter as tk
from tkinter import TclError, ttk

def creat_input_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    ttk.Label(frame, text='find what:').grid(column=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    ttk.Label(frame, text='Replace width:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    math_case = tk.StringVar()
    math_case_check = ttk.Checkbutton(frame, text='Match case', variable=math_case, command=lambda:print(math_case.get()))
    math_case_check.grid(column=0, row=2, sticky=tk.W)

    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(frame, variable=wrap_around, text='Wrap around', command=lambda:print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Camcel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_main_window():
    root = tk.Tk()
    root.title('Replace')
    root.resizable(0,0)
    try:
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = creat_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()

if __name__ == '__main__':
    create_main_window()