import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

frame = ttk.Frame(window, width=100, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(True)
frame.pack()

label = ttk.Label(frame, text='Label in frame')
label.pack()

button = ttk.Button(frame, text='button in a frame')
button.pack()

window.mainloop()