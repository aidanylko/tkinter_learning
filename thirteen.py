import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Pack methods')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Label 3', background='green')
button = ttk.Button(window, text='Button')

# label1.pack(side='right')
# label2.pack(side='left')
# label3.pack(side='left')
# button.pack(side='left')

label1.pack(side='top', expand=True, fill='both', padx=10, pady=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', fill='both')


window.mainloop()