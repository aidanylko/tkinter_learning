import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


window = tk.Tk()
window.title('Sliders')

scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    window,
    command=lambda value: print(scale_float.get()),
    from_=0,
    to=25,
    length=300,
    orient='vertical',
    variable=scale_float)
scale.pack()

progress = ttk.Progressbar(window, variable=scale_float, maximum=25)
progress.pack()

# Scrolled text
scroll = scrolledtext.ScrolledText(window, width=100, height=5)
scroll.pack()

window.mainloop()
