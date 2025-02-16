import tkinter as tk
from tkinter import ttk


def button_func():
    print('a button was pressed')


def hello_button():
    print('Hello!')


# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x600')

# create widgets
text = tk.Text(master=window)
text.pack()

# ttk widgets
label = ttk.Label(master=window, text='This is label')
label.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text='Button', command=button_func)
button.pack()

# ttk entry
entry1 = ttk.Entry(master=window)
entry1.pack()

# ttk widgets
label1 = ttk.Label(master=window, text='This is another label')
label1.pack()

# ttk button
button1 = ttk.Button(master=window, text='Button hello', command=hello_button)
button1.pack()

# run
window.mainloop()
