from tkinter import *
import tkinter as tk 
from PIL import ImageTk, Image
from matplotlib.ft2font import BOLD




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
    def get_pic(our_pic):#,n,m
        pic = Image.open(our_pic)
        
        
        
        # pic_res = pic.resize((n,m))
        imgo = ImageTk.PhotoImage(pic)
        return imgo

    # img = get_pic("scint_1.png")
    # frame = Frame(s_books, width=200, height=200)
    # frame.pack()
    
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

    def get_pic(our_pic):#,n,m
        pic = Image.open(our_pic)
    
        imgo = ImageTk.PhotoImage(pic)
        return imgo
   
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

    def get_pic(our_pic):#,n,m
        pic = Image.open(our_pic)
    
        imgo = ImageTk.PhotoImage(pic)
        return imgo

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
    global img18,img19,img20,img21,img22,img23
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
    Label(b_books,text = "Simple Numbers, Straight Talk!",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
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

    def get_pic(our_pic):#,n,m
        pic = Image.open(our_pic)
    
        imgo = ImageTk.PhotoImage(pic)
        return imgo
    
    img18 = ImageTk.PhotoImage(Image.open("source\\img18.jpg"))
    Label(b_books,image=img18).place(x=40,y=90)

    img19 = ImageTk.PhotoImage(Image.open("source\\img19.jpg"))
    Label(b_books,image=img19).place(x=260,y=90)

    img20 = ImageTk.PhotoImage(Image.open("source\\img20.jpg"))
    Label(b_books,image=img20).place(x=490,y=75)

    img21 = ImageTk.PhotoImage(Image.open("source\\img21.jpg"))
    Label(b_books,image=img21).place(x=30,y=375)

    img22 = ImageTk.PhotoImage(Image.open("source\\img22.jpg"))
    Label(b_books,image=img22).place(x=260,y=385)

    img23 = ImageTk.PhotoImage(Image.open("source\\img23.jpg"))
    Label(b_books,image=img23).place(x=490,y=385)


def for_kids():
    global k_books
    global img24,img25,img26,img27,img28,img29
    k_books = Toplevel(category_screen)
    k_books.title("Business_books")
    k_books.geometry("700x800")
    k_books["bg"] = "white" 
    Label(k_books,text = "BOOKS FOR KIDS",font =("Times",20),bg = "white").place(x = 225,y=25)


    Label(k_books,text = "Don't Let the Pigeon Drive!",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 250)
    Label(k_books,text = "Authors:Mo Willems",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 270)
    Label(k_books,text = "Category:For kids",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 290)
    Label(k_books,text = "Number:50",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 310)
    Button(k_books,text = "Description",font = ("Times",8),bg = "white",fg = "red",command=short_history).place(x = 15,y =330)
    #2
    Label(k_books,text = "Goodnight,Construction Site",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 250)
    Label(k_books,text = "Authors:Sherri Duskey Rinker ",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 270)
    Label(k_books,text = "Category:For kids",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 290)
    Label(k_books,text = "Number:51",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 310)
    Button(k_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
    #3
    Label(k_books,text = "The Snowy Day",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
    Label(k_books,text = "Authors:Ezra Jack Keats",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 270)
    Label(k_books,text = "Category:For kids",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 290)
    Label(k_books,text = "Number:52",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 310)
    Button(k_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
    #4
    Label(k_books,text = "The Very Hungry Caterpillar",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 570)
    Label(k_books,text = "Authors:Eric Carle ",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 590)
    Label(k_books,text = "Category:For kids",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 610)
    Label(k_books,text = "Number:53",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 630)
    Button(k_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
    #5
    Label(k_books,text = "Where the Wild Things Are",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 570)
    Label(k_books,text = "Authors:Maurice Sendak ",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 590)
    Label(k_books,text = "Category:For kids",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 610)
    Label(k_books,text = "Number:54",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 630)
    Button(k_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
    #6
    Label(k_books,text = "The Tale of Peter Rabbit",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 570)
    Label(k_books,text = "Authors:Beatrix Potter",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 590)
    Label(k_books,text = "Category:For kids",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 610)
    Label(k_books,text = "Number:55",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 630)
    Button(k_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

    def get_pic(our_pic):#,n,m
        pic = Image.open(our_pic)
    
        imgo = ImageTk.PhotoImage(pic)
        return imgo
    
    img24 = ImageTk.PhotoImage(Image.open("source\\img24.jpg"))
    Label(k_books,image=img24).place(x=30,y=100)

    img25 = ImageTk.PhotoImage(Image.open("source\\img25.jpg"))
    Label(k_books,image=img25).place(x=260,y=110)

    img26 = ImageTk.PhotoImage(Image.open("source\\img26.jpg"))
    Label(k_books,image=img26).place(x=490,y=130)

    img27 = ImageTk.PhotoImage(Image.open("source\\img27.jpg"))
    Label(k_books,image=img27).place(x=30,y=430)

    img28 = ImageTk.PhotoImage(Image.open("source\\img28.jpg"))
    Label(k_books,image=img28).place(x=260,y=450)

    img29 = ImageTk.PhotoImage(Image.open("source\\img29.jpg"))
    Label(k_books,image=img29).place(x=490,y=430)


def psychologic():
    global p_books
    global img30,img31,img32,img33,img34,img35
    p_books = Toplevel(category_screen)
    p_books.title("Business_books")
    p_books.geometry("700x800")
    p_books["bg"] = "white" 
    Label(p_books,text = "PSYCHOLOGY BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)


    Label(p_books,text = "The Happiness Hypothesis",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 250)
    Label(p_books,text = "Authors:Jonathan Haidt",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 270)
    Label(p_books,text = "Category:Psychology",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 290)
    Label(p_books,text = "Number:60",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 310)
    Button(p_books,text = "Description",font = ("Times",8),bg = "white",fg = "red",command=short_history).place(x = 15,y =330)
    #2
    Label(p_books,text = "The Psychology of Persuasion",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 250)
    Label(p_books,text = "Authors:Robert B. Cialdini",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 270)
    Label(p_books,text = "Category:Phychology",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 290)
    Label(p_books,text = "Number:61",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 310)
    Button(p_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
    #3
    Label(p_books,text = "Mistakes Were Made",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
    Label(p_books,text = "Authors:Carol Tavris",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 270)
    Label(p_books,text = "Category:Psychology",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 290)
    Label(p_books,text = "Number:62",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 310)
    Button(p_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
    #4
    Label(p_books,text = "How to Solve Problems",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 570)
    Label(p_books,text = "Authors:Dan Heath ",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 590)
    Label(p_books,text = "Category:Psychology",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 610)
    Label(p_books,text = "Number:63",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 630)
    Button(p_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
    #5
    Label(p_books,text = "The School of Life",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 570)
    Label(p_books,text = "Authors:Alain de Botton ",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 590)
    Label(p_books,text = "Category:Psychology",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 610)
    Label(p_books,text = "Number:64",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 630)
    Button(p_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
    #6
    Label(p_books,text = "The Body Keeps the Score",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 570)
    Label(p_books,text = "Authors:Bessel Van Der Kolk",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 590)
    Label(p_books,text = "Category:Psychology",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 610)
    Label(p_books,text = "Number:65",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 630)
    Button(p_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

    def get_pic(our_pic):#,n,m
        pic = Image.open(our_pic)
    
        imgo = ImageTk.PhotoImage(pic)
        return imgo
    
    img30 = ImageTk.PhotoImage(Image.open("source\\img30.jpg"))
    Label(p_books,image=img30).place(x=30,y=90)

    img31 = ImageTk.PhotoImage(Image.open("source\\img31.jpg"))
    Label(p_books,image=img31).place(x=260,y=70)

    img32 = ImageTk.PhotoImage(Image.open("source\\img32.jpg"))
    Label(p_books,image=img32).place(x=490,y=70)

    img33 = ImageTk.PhotoImage(Image.open("source\\img33.jpg"))
    Label(p_books,image=img33).place(x=30,y=380)

    img34 = ImageTk.PhotoImage(Image.open("source\\img34.jpg"))
    Label(p_books,image=img34).place(x=250,y=380)

    img35 = ImageTk.PhotoImage(Image.open("source\\img35.jpg"))
    Label(p_books,image=img35).place(x=490,y=380)


def novels():
    global n_books
    global img36,img37,img38,img39,img40,img41
    n_books = Toplevel(category_screen)
    n_books.title("Novels")
    n_books.geometry("700x800")
    n_books["bg"] = "white" 
    Label(n_books,text = "NOVELS",font =("Times",20),bg = "white").place(x = 250,y=15)


    Label(n_books,text = "The Pilgrims Progress",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 250)
    Label(n_books,text = "Authors:John Bunyan",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 270)
    Label(n_books,text = "Category:Novel",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 290)
    Label(n_books,text = "Number:70",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 310)
    Button(n_books,text = "Description",font = ("Times",8),bg = "white",fg = "red",command=short_history).place(x = 15,y =330)
    #2
    Label(n_books,text = "Robinson Crusoe",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 250)
    Label(n_books,text = "Authors:Daniel Defoe",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 270)
    Label(n_books,text = "Category:Novel",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 290)
    Label(n_books,text = "Number:71",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 310)
    Button(n_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
    #3
    Label(n_books,text = "Gullivers Travels",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 250)
    Label(n_books,text = "Authors:Jonathan Swift",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 270)
    Label(n_books,text = "Category:Novel",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 290)
    Label(n_books,text = "Number:72",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 310)
    Button(n_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
    #4
    Label(n_books,text = "Clarissa",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15,y = 570)
    Label(n_books,text = "Authors:Samuel Richardson ",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 590)
    Label(n_books,text = "Category:Novel",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 610)
    Label(n_books,text = "Number:73",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 15,y = 630)
    Button(n_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
    #5
    Label(n_books,text = "Tom Jones",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240,y = 570)
    Label(n_books,text = "Authors:Henry Fielding",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 590)
    Label(n_books,text = "Category:Novel",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 610)
    Label(n_books,text = "Number:74",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 240,y = 630)
    Button(n_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
    #6
    Label(n_books,text = "Emma",font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480,y = 570)
    Label(n_books,text = "Authors:Jane Austen",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 590)
    Label(n_books,text = "Category:Novel",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 610)
    Label(n_books,text = "Number:75",font = ("Times",8),bg = "light sky blue",fg = "black").place(x = 480,y = 630)
    Button(n_books,text = "Description",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

    def get_pic(our_pic):#,n,m
        pic = Image.open(our_pic)
    
        imgo = ImageTk.PhotoImage(pic)
        return imgo
    
    img36 = ImageTk.PhotoImage(Image.open("source\\img36.jpg"))
    Label(n_books,image=img36).place(x=25,y=60)

    img37 = ImageTk.PhotoImage(Image.open("source\\img37.jpg"))
    Label(n_books,image=img37).place(x=240,y=60)

    img38 = ImageTk.PhotoImage(Image.open("source\\img38.jpg"))
    Label(n_books,image=img38).place(x=490,y=60)

    img39 = ImageTk.PhotoImage(Image.open("source\\img39.jpg"))
    Label(n_books,image=img39).place(x=25,y=380)

    img40 = ImageTk.PhotoImage(Image.open("source\\img40.jpg"))
    Label(n_books,image=img40).place(x=240,y=380)

    img41 = ImageTk.PhotoImage(Image.open("source\\img41.jpg"))
    Label(n_books,image=img41).place(x=490,y=380)



    


        







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
Button(category_screen, text = "FOR KIDS" ,width = 25, height = 10,bg = "white",command=for_kids).place(x = 250,y = 300)
Button(category_screen, text = "PSYCHOLOGY" ,width = 25, height = 10,bg = "white",command=psychologic).place(x = 480,y = 300)

Button(category_screen, text = "NOVELS" ,width = 25, height = 10,bg = "white",command=novels).place(x = 250,y = 500)


# Label(category_screen,image=img).place(x=100,y=100)
category_screen.mainloop()