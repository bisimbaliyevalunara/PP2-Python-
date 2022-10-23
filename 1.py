from tkinter import *
from PIL import ImageTk, Image

root = Tk()
img13 = ImageTk.PhotoImage(Image.open("source\\img13.jpg"))
txt = Text(root)
txt.insert(END, "A Brief History of Time plunges into the exotic realms of black holes and quarks, of antimatter and “arrows of time,” of the big bang and a bigger God—where the possibilities are wondrous and unexpected. With exciting images and profound imagination, Stephen Hawking brings us closer to the ultimate secrets at the very heart of creation")
Label(root, text = f"{txt}",  image = img13, compound = "top").pack()
root.mainloop()
