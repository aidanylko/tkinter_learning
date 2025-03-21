import tkinter as tk
from tkinter import ttk


def button_func():
    print(string_var.get())
    string_var.set('button_pressed')


window = tk.Tk()
window.title('Tkinter variables')


string_var = tk.StringVar()

label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()
entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='Button', command=button_func)
button.pack()

exercise_var = tk.StringVar(value='test')

entry1 = ttk.Entry(master=window, textvariable=exercise_var)
entry1.pack()
entry2 = ttk.Entry(master=window, textvariable=exercise_var)
entry2.pack()

exercise_label = ttk.Label(master=window, textvariable=exercise_var)
exercise_label.pack()

window.mainloop()
