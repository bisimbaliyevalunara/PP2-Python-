from tkinter import *
from PIL import Image, ImageTk


root = Tk()

image = ImageTk.PhotoImage(Image.open("source\\img36.jpg")) 

Label(root, text='Hello', image=image, compound='bottom').pack()

root.mainloop()