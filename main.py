from gui import MainGui
import tkinter as tk


window = tk.Tk()
main = MainGui(window)
window.title('Register your products')
window.geometry('700x600+10+10')
window.mainloop()
