import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('600x400')
window.title('Tab widgets')

notebook = ttk.Notebook(window)

# tab1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text='Button in tab 1')
button1.pack()

# tab2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='Text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')

# tab3
tab3 = ttk.Frame(notebook)
button3 = ttk.Button(tab3, text='button3')
button3.pack()
label3 = ttk.Label(tab3, text='Text in tab3')
label3.pack()
notebook.add(tab3, text='Tab3')
notebook.pack()
window.mainloop()
