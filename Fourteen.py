import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('pack parenting')
window.geometry('400x600')

top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='First label', background='red')
label2 = ttk.Label(top_frame, text='Label 2', background='blue')

label3 = ttk.Label(window, text='another label', background='green')

bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text='Last of the labels', background='orange')
button1 = ttk.Button(bottom_frame, text='A Button')
button2 = ttk.Button(bottom_frame, text='Another button')

exersice_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(exersice_frame, text='Button 3')
button4 = ttk.Button(exersice_frame, text='Button 4')
button5 = ttk.Button(exersice_frame, text='Button 5')

label1.pack(side='left',fill='both', expand=True)
label2.pack(side='left', fill='both', expand=True)
top_frame.pack(fill='both', expand=True)

label3.pack(expand=True)

button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)

button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
exersice_frame.pack(side='left', fill='both', expand=True)
window.mainloop()
