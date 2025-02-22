import tkinter as tk
from tkinter import ttk


def button_func():
    print('a basic button')


# setup
window = tk.Tk()
window.title('Combo and Spin')
window.geometry('600x400')


# combobox
items = ['ice cream', 'pizza', 'broccoli']
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable= food_string)
# combo['values'] = items
combo.configure(values=items)
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'Selected value: {food_string.get()}'))
combo_label = ttk.Label(window, text='a label', textvariable= food_string)
combo_label.pack()

# Spinbox
#spin = ttk.Spinbox(window, from_=3, to=20, increment=1, command=lambda: print('a arrow was pressed'))
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(
    window,
    from_=3,
    to=20,
    increment=3,
    command=lambda: print('a arrow was pressed'),
    textvariable=spin_int)

spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()

exercise_letters = ['A', 'B', 'C', 'D', 'E']
exercise_string = tk.StringVar(value=exercise_letters[0])
exercise_spin = ttk.Spinbox(window, textvariable=exercise_string)
exercise_spin['values']=exercise_letters
exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_string.get()))
exercise_spin.pack()

# run
window.mainloop()