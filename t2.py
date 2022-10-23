from tkinter import *
import tkinter as tk 
from PIL import ImageTk, Image




def scientific():
    global s_books
    global img,img1,img2,img3,img4,img5,img8
    s_books = Toplevel(category_screen)
    # s_books = Tk()
    s_books.title("SCIENTIFIC_BOOKS")
    s_books.geometry("700x800")
    s_books["bg"] = "white" 
    Label(s_books,text = "SCIENTIFIC BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)
    

    #1
    Label(s_books,text = "A Brief History of Time",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 250)
    Label(s_books,text = "Authors:Stephen Hawking, Leonard Mlodinov",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 270)
    Label(s_books,text = "Category:Scientific and Education",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 290)
    Label(s_books,text = "Number:3",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 310)
    Button(s_books,text = "Description",font = ("Times",8),bg = "white",fg = "red",command=short_history).place(x = 15,y =330)
    #2
    Label(s_books,text = "Women in Science: 50 Fearless Pioneers",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 250)
    Label(s_books,text = "Authors:Rachel Ignotofsky",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 270)
    Label(s_books,text = "Category:Scientific and Education",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 290)
    Label(s_books,text = "Number:7",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 310)
    Button(s_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
    #3
    Label(s_books,text = "A brief history of mankind",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
    Label(s_books,text = "Authors:Yoval Noah Harari",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 270)
    Label(s_books,text = "Category:Scientific and Education",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 290)
    Label(s_books,text = "Number:8",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 310)
    Button(s_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
    #4
    Label(s_books,text = "The History of Ancient Rome",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 570)
    Label(s_books,text = "Authors:Mary Baird",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 590)
    Label(s_books,text = "Category:Scientific and Education",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 610)
    Label(s_books,text = "Number:9",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 630)
    Button(s_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
    #5
    Label(s_books,text = "The Apology of mathematics",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 570)
    Label(s_books,text = "Authors:Vladimir Uspensky",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 590)
    Label(s_books,text = "Category:Scientific and Education",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 610)
    Label(s_books,text = "Number:23",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 630)
    Button(s_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
    #6
    Label(s_books,text = "Astronomy in 30 seconds",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 570)
    Label(s_books,text = "Authors:Francois Fressen",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 590)
    Label(s_books,text = "Category:Scientific and Education",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 610)
    Label(s_books,text = "Number:29",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 630)
    Button(s_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)
    
    img = ImageTk.PhotoImage(Image.open("source\\hist.jpg"))
    Label(s_books,image=img).place(x=60,y=70)

    img1 = ImageTk.PhotoImage(Image.open("source\\wom.jpeg"))
    Label(s_books,image=img1).place(x=260,y=60)

    img2 = ImageTk.PhotoImage(Image.open("source\\scient.jpg"))
    Label(s_books,image=img2).place(x=480,y=80)

    img3 = ImageTk.PhotoImage(Image.open("source\\rom1.jpg"))
    Label(s_books,image=img3).place(x=50,y=415)

    img4 = ImageTk.PhotoImage(Image.open("source\\math.jpg"))
    Label(s_books,image=img4).place(x=260,y=405)

    img5 = ImageTk.PhotoImage(Image.open("source\\space.jpg"))
    Label(s_books,image=img5).place(x=480,y=405)


def short_history():
    global description,img8
    description = Toplevel(s_books)
    description.title("Description")
    description.geometry("500x700")
    

def adventure():
    global a_books
    global img6,img7,img8,img9,img10,img11
    a_books = Toplevel(category_screen)
    a_books.title("Adventure_books")
    a_books.geometry("700x800")
    a_books["bg"] = "white" 
    Label(a_books,text = "ADVANTURE BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)


    Label(a_books,text = "The Three Musketeers",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 250)
    Label(a_books,text = "Authors:Alexandre Dumas",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 270)
    Label(a_books,text = "Category:Adventure",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 290)
    Label(a_books,text = "Number:20",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 310)
    Button(a_books,text = "Description",font = ("Times",8),bg = "white",fg = "red",command=short_history).place(x = 15,y =330)
    #2
    Label(a_books,text = "Treasure Island",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 250)
    Label(a_books,text = "Authors:Robert Louis Stevenson",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 270)
    Label(a_books,text = "Category:Adventure",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 290)
    Label(a_books,text = "Number:21",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 310)
    Button(a_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
    #3
    Label(a_books,text = "King Solomon's Mines",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
    Label(a_books,text = "Authors:H. Rider Haggard,A. C. Michael",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 270)
    Label(a_books,text = "Category:Adventure",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 290)
    Label(a_books,text = "Number:22",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 310)
    Button(a_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
    #4
    Label(a_books,text = "Journey to the Center of the Earth ",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 570)
    Label(a_books,text = "Authors:Jules Verne",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 590)
    Label(a_books,text = "Category:Adventure",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 610)
    Label(a_books,text = "Number:23",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 630)
    Button(a_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
    #5
    Label(a_books,text = "The Count of Monte Cristo",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 570)
    Label(a_books,text = "Authors:Alexandre Dumas",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 590)
    Label(a_books,text = "Category:Adventure",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 610)
    Label(a_books,text = "Number:24",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 630)
    Button(a_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
    #6
    Label(a_books,text = "Ivanhoe",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 570)
    Label(a_books,text = "Authors:Walter Scott",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 590)
    Label(a_books,text = "Category:Adventure",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 610)
    Label(a_books,text = "Number:25",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 630)
    Button(a_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)
   
    img6 = ImageTk.PhotoImage(Image.open("source\\mus.jpg"))
    Label(a_books,image=img6).place(x=40,y=80)

    img7 = ImageTk.PhotoImage(Image.open("source\\island.jpg"))
    Label(a_books,image=img7).place(x=260,y=80)

    img8 = ImageTk.PhotoImage(Image.open("source\\king.jpg"))
    Label(a_books,image=img8).place(x=490,y=80)

    img9 = ImageTk.PhotoImage(Image.open("source\\img9.jpg"))
    Label(a_books,image=img9).place(x=40,y=365)

    img10 = ImageTk.PhotoImage(Image.open("source\\cou.jpg"))
    Label(a_books,image=img10).place(x=260,y=365)

    img11 = ImageTk.PhotoImage(Image.open("source\\ivan.jpg"))
    Label(a_books,image=img11).place(x=490,y=365)

    
def fantastic():
    global f_books
    global img12,img13,img14,img15,img16,img17
    f_books = Toplevel(category_screen)
    f_books.title("Fantastic_books")
    f_books.geometry("700x800")
    f_books["bg"] = "white" 
    Label(f_books,text = "FANTASY BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)

    Label(f_books,text = "LE MORTE DARTHUR",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 250)
    Label(f_books,text = "Authors:Thomas Malory",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 270)
    Label(f_books,text = "Category:Fantasy",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 290)
    Label(f_books,text = "Number:30",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 310)
    Button(f_books,text = "Description",font = ("Times",8),bg = "white",fg = "red",command=short_history).place(x = 15,y =330)
    #2
    Label(f_books,text = "Stardust",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 250)
    Label(f_books,text = "Authors:Neil Gaiman",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 270)
    Label(f_books,text = "Category:Fantasy",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 290)
    Label(f_books,text = "Number:31",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 310)
    Button(f_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
    #3
    Label(f_books,text = "Jade City",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
    Label(f_books,text = "Authors:Fonda Lee",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 270)
    Label(f_books,text = "Category:Fantasy",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 290)
    Label(f_books,text = "Number:32",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 310)
    Button(f_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
    #4
    Label(f_books,text = "The Last Unicorn ",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 570)
    Label(f_books,text = "Authors:Peter S Beagle",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 590)
    Label(f_books,text = "Category:Fantasy",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 610)
    Label(f_books,text = "Number:33",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 630)
    Button(f_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
    #5
    Label(f_books,text = "Who Fears Death",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 570)
    Label(f_books,text = "Authors:Nnedi Okorafor",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 590)
    Label(f_books,text = "Category:Fantasy",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 610)
    Label(f_books,text = "Number:34",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 630)
    Button(f_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
    #6
    Label(f_books,text = "The Power",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 570)
    Label(f_books,text = "Authors:Naomi Alderman",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 590)
    Label(f_books,text = "Category:Fantasy",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 610)
    Label(f_books,text = "Number:35",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 630)
    Button(f_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

    img12 = ImageTk.PhotoImage(Image.open("source\\img12.jpg"))
    Label(f_books,image=img12).place(x=25,y=55)

    img13 = ImageTk.PhotoImage(Image.open("source\\img13.jpg"))
    Label(f_books,image=img13).place(x=250,y=80)

    img14 = ImageTk.PhotoImage(Image.open("source\\city.jpg"))
    Label(f_books,image=img14).place(x=450,y=80)

    img15 = ImageTk.PhotoImage(Image.open("source\\image_15.jpg"))
    Label(f_books,image=img15).place(x=25,y=405)

    img16 = ImageTk.PhotoImage(Image.open("source\\img16.jpg"))
    Label(f_books,image=img16).place(x=230,y=405)

    img17 = ImageTk.PhotoImage(Image.open("source\\img17.jpg"))
    Label(f_books,image=img17).place(x=470,y=405)


def business():
    global b_books
    global img18
    b_books = Toplevel(category_screen)
    b_books.title("Business_books")
    b_books.geometry("700x800")
    b_books["bg"] = "white" 
    Label(b_books,text = "BUSINESS BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)


    Label(b_books,text = "Fooled by Randomness",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 250)
    Label(b_books,text = "Authors: Nassim Nicholas Taleb",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 270)
    Label(b_books,text = "Category:Business",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 290)
    Label(b_books,text = "Number:40",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 310)
    Button(b_books,text = "Description",font = ("Times",8),bg = "white",fg = "red",command=short_history).place(x = 15,y =330)
    #2
    Label(b_books,text = "Breakthrough Advertising",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 250)
    Label(b_books,text = "Authors:Eugene Schwartz",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 270)
    Label(b_books,text = "Category:Business",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 290)
    Label(b_books,text = "Number:41",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 310)
    Button(b_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
    #3
    Label(b_books,text = "Simple Numbers, Straight Talk, Big Profits!",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
    Label(b_books,text = "Authors:Greg Crabtree",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 270)
    Label(b_books,text = "Category:Business",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 290)
    Label(b_books,text = "Number:42",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 310)
    Button(b_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
    #4
    Label(b_books,text = "How to Win Friends & Influence People ",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 570)
    Label(b_books,text = "Authors:Dale Carnegie",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 590)
    Label(b_books,text = "Category:Business",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 610)
    Label(b_books,text = "Number:43",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 630)
    Button(b_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
    #5
    Label(b_books,text = "The 22 Immutable Laws of Marketing",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 570)
    Label(b_books,text = "Authors:Al Ries,Jack Trout",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 590)
    Label(b_books,text = "Category:Business",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 610)
    Label(b_books,text = "Number:44",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 630)
    Button(b_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
    #6
    Label(b_books,text = "Business Adventures",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 570)
    Label(b_books,text = "Authors:John Brooks",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 590)
    Label(b_books,text = "Category:Business",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 610)
    Label(b_books,text = "Number:45",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 630)
    Button(b_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)


category_screen = Tk()
category_screen.title("Library")
category_screen.geometry("700x800")
path = 'source\\BOOK CATEGORIES.png'
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(category_screen, image = img)
panel.place(x=0, y=0, relwidth=1, relheight=1)
# img = ImageTk.PhotoImage(Image.open("Description.png"))


Button(category_screen, text = "SCIENTIFIC AND EDUCATIONAL" ,width = 25, height = 10, bg = "white",command=scientific).place(x = 30,y = 100)
Button(category_screen, text = "ADVENTURES" ,width = 25, height = 10,bg = "white",command=adventure).place(x = 250,y = 100)
Button(category_screen, text = "FANTASTIC" ,width = 25, height = 10,bg = "white",command=fantastic).place(x = 480,y = 100)

Button(category_screen, text = "BUSINESS" ,width = 25, height = 10,bg = "white",command=business).place(x = 30,y = 300)
Button(category_screen, text = "FOR KIDS" ,width = 25, height = 10,bg = "white").place(x = 250,y = 300)
Button(category_screen, text = "PSYCHOLOGY" ,width = 25, height = 10,bg = "white").place(x = 480,y = 300)

Button(category_screen, text = "NOVELS" ,width = 25, height = 10,bg = "white").place(x = 250,y = 500)


# Label(category_screen,image=img).place(x=100,y=100)
category_screen.mainloop()