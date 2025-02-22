import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f'x: {event.x} y: {event.y}')


# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='A button')
button.pack()

# event
button.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
window.bind('<Motion>', get_pos)

window.bind('<KeyPress>', lambda event: print(f'a button was pressed {event.char}'))

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was selected'))

text.bind('<Shift-MouseWheel>', lambda event: print('mousewheel'))
# run
window.mainloop()