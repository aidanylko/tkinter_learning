import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('600x400')
window.title('Sliders')

# menu
menu = tk.Menu(window)
# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda: print('New File'))
file_menu.add_command(label='open', command=lambda: print('Open File'))
file_menu.add_separator()
menu.add_cascade(label='File', menu=file_menu)

# another sub menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help entry', command=lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=help_check_string)

menu.add_cascade(label='Help', menu=help_menu)

# menu button
menu_button = ttk.Menubutton(window, text='Menu Button')
menu_button.pack()
button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label='entry 1', command=lambda: print('test 1'))
menu_button.configure(menu=button_sub_menu)

window.configure(menu=menu)
# run
window.mainloop()