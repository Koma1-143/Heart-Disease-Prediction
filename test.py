import sys
from tkinter import messagebox

from tkinter import *
import time

Window = Tk()
Window.geometry("800x600")
Window.title("Warning")
messagebox.showinfo("warning","The Person might have a Heart Disease")
Window.destroy()
Window.mainloop()