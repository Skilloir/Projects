from tkinter import *
import tkinter as tk
r = tk.Tk()
r.title('Cookie Clicker')
header = tk.Text('test')
button = tk.Button(r, text='Click', width=100, command=r.destroy)
button.pack()
r.mainloop()