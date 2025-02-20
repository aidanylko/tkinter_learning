import tkinter as tk
from tkinter import ttk


def button_func():
    print('a basic button')


# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
button_string = tk.StringVar(value='a button with a string var')
button = ttk.Button(window, text='A simple button', command=button_func, textvariable=button_string)
button.pack()

# check button
check_var = tk.IntVar()
check = ttk.Checkbutton(window, text='checkbox 1', command=lambda:print(type(check_var.get())), variable=check_var)
check.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text='Radiobutton 1',
    value='radio1',
    variable=radio_var,
    command=lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(
    window,
    text='Radiobutton 2',
    value=2,
    variable=radio_var,
    command=lambda: print(radio_var.get()))
radio2.pack()
# run
window.mainloop()