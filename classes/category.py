from tkinter import *
from PIL import ImageTk, Image

class Category:
    def __init__(self, db, user): # we need to take user id
        self.db = db
        # self.db = Database()
        self.user = user
        self.user_full_info = self.db.get_user_by_login(self.user)[0]
        self.user_id = self.user_full_info[0]
        print(self.user_full_info)

    def start(self):
        self.category_screen = Tk()
        self.category_screen.title("Library")
        self.category_screen.geometry("700x800+300+0")
        self.category_screen.resizable(False, False)
        self.state = False
        # self.user_full_info = self.db
        image = ImageTk.PhotoImage(Image.open("source\\BOOK CATEGORIES.png"))
        Label(self.category_screen, image = image).place(x = 0, y = 0, relwidth = 1, relheight = 1)
        frame = Frame(self.category_screen, width = 150, height = 50)
        Label(frame, text = f"user: {self.user}").place(x = 5, y = 5)
        Label(frame, text = f"status: {self.user_full_info[-1]}").place(x = 5, y = 25)
        frame.place(x = 5, y = 5)


        Button(self.category_screen, text = "Log out", command = self.back_to_register).place(x = 640, y = 5)
        if self.user_full_info[-1] == "student": Button(self.category_screen, text = "Return book", command = self.return_book).pack()
        else: Button(self.category_screen, text = "Publish book", command = self.publish_book).pack()
        Button(self.category_screen, text = "SCIENTIFIC AND EDUCATIONAL", width = 25, height = 10, command = self.scientific).place(x = 30, y = 100)
        Button(self.category_screen, text = "ADVENTURES", width = 25, height = 10, command = self.adventure).place(x = 250, y = 100)
        Button(self.category_screen, text = "FANTASTIC", width = 25, height = 10, command = self.fantastic).place(x = 480, y = 100)
        Button(self.category_screen, text = "BUSINESS", width = 25, height = 10, command=self.business).place(x = 30, y = 300)
        Button(self.category_screen, text = "FOR KIDS", width = 25, height = 10, command=self.for_kids).place(x = 250, y = 300)
        Button(self.category_screen, text = "PSYCHOLOGY", width = 25, height = 10, command=self.psychologic).place(x = 480, y = 300)
        Button(self.category_screen, text = "NOVELS", width = 25, height = 10, command=self.novels).place(x = 250, y = 500)

        self.category_screen.mainloop()

    def return_book(self): 
        global return_book_screen
        return_book_screen = Toplevel(self.category_screen)

    def publish_book(self): pass

    def check(self, book_id):
        if self.db.check_amount_of_book(book_id, number.get()):
            print("yeah, number of books is enough!")
            self.db.update_amount_of_book(book_id, number.get())
        else: print("Not enough(")
        # self.db.update_and_check_amount_of_book(book_id, number.get())

    def borrow_the_book(self, book_id, book_number): 
        global borrow_book_screen
        global number
        borrow_book_screen = Toplevel(self.category_screen)
        Label(borrow_book_screen, text = "Number: ").pack(side = LEFT)
        number = Entry(borrow_book_screen); number.pack()
        # if book_id >= int(number.get()): self.db.update_amount_of_book(book_id, book_number - int(number.get()))
        Button(borrow_book_screen, text = "OK", command = lambda: self.check(book_id)).pack()

    def books(self):
        global books_screen
        books_screen = Toplevel(self.category_screen)
        books_screen.geometry("700x800+300+0")
        books_screen.resizable(False, False)
        scrollbar = Scrollbar(books_screen)
        scrollbar.pack(side = RIGHT, fill = Y)
        books = Listbox(books_screen, yscrollcommand = scrollbar.set)
        for line in range(200):
            books.insert(END, "This is line number " + str(line))
        books.pack(side = LEFT, fill = BOTH)
        scrollbar.config(command = books.yview)

    def back_to_register(self):
        self.state = True
        self.category_screen.destroy()

    def scientific(self):
        global s_books
        global img,img1,img2,img3,img4,img5,img8
        s_books = Toplevel(self.category_screen)
        # s_books = Tk()
        s_books.title("SCIENTIFIC_BOOKS")
        s_books.geometry("700x800+300+0")
        s_books["bg"] = "white" 
        books = self.db.get_books_by_category("Scientific and Education")
        print(books)

        Label(s_books,text = "SCIENTIFIC BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)

        Label(s_books, text = f"Id: {books[0][0]}\n{books[0][1]}\nAuthors: {books[0][2]}\nCategory: {books[0][3]}\nNumber: {books[0][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 250)
        Label(s_books, text = f"Id: {books[1][0]}\n{books[1][1]}\nAuthors: {books[1][2]}\nCategory: {books[1][3]}\nNumber: {books[1][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 250)
        Label(s_books, text = f"Id: {books[2][0]}\n{books[2][1]}\nAuthors: {books[2][2]}\nCategory: {books[2][3]}\nNumber: {books[2][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 250)
        Label(s_books, text = f"Id: {books[3][0]}\n{books[3][1]}\nAuthors: {books[3][2]}\nCategory: {books[3][3]}\nNumber: {books[3][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 570)
        Label(s_books, text = f"Id: {books[4][0]}\n{books[4][1]}\nAuthors: {books[4][2]}\nCategory: {books[4][3]}\nNumber: {books[4][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 570)
        Label(s_books, text = f"Id: {books[5][0]}\n{books[5][1]}\nAuthors: {books[5][2]}\nCategory: {books[5][3]}\nNumber: {books[5][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 570)

        Button(s_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red",command=lambda: self.short_history(n_books)).place(x = 15,y =330)
        Button(s_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
        Button(s_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
        Button(s_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
        Button(s_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
        Button(s_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

        Button(s_books, text = "Borrow", command = lambda: self.borrow_the_book(books[0][0], books[0][4])).place(x = 130, y = 330)


        img = ImageTk.PhotoImage(Image.open(books[0][-2]))
        Label(s_books,text="qwertyuiopasdfghjklzxcvbnm", image=img).place(x=60,y=70)

        img1 = ImageTk.PhotoImage(Image.open(books[1][-2]))
        Button(s_books,image=img1, command=lambda: self.short_history(s_books)).place(x=260,y=60)

        img2 = ImageTk.PhotoImage(Image.open(books[2][-2]))
        Label(s_books,image=img2).place(x=480,y=80)

        img3 = ImageTk.PhotoImage(Image.open(books[3][-2]))
        Label(s_books,image=img3).place(x=50,y=415)

        img4 = ImageTk.PhotoImage(Image.open(books[4][-2]))
        Label(s_books,image=img4).place(x=260,y=405)

        img5 = ImageTk.PhotoImage(Image.open(books[5][-2]))
        Label(s_books,image=img5).place(x=480,y=405)

    def adventure(self):
        global a_books
        global img6,img7,img8,img9,img10,img11
        a_books = Toplevel(self.category_screen)
        a_books.title("Adventure_books")
        a_books.geometry("700x800+300+0")
        a_books["bg"] = "white" 
        books = self.db.get_books_by_category("Adventure")
        print(books)

        Label(a_books,text = "ADVANTURE BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)

        Label(a_books, text = f"Id: {books[0][0]}\n{books[0][1]}\nAuthors: {books[0][2]}\nCategory: {books[0][3]}\nNumber: {books[0][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 250)
        Label(a_books, text = f"Id: {books[1][0]}\n{books[1][1]}\nAuthors: {books[1][2]}\nCategory: {books[1][3]}\nNumber: {books[1][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 250)
        Label(a_books, text = f"Id: {books[2][0]}\n{books[2][1]}\nAuthors: {books[2][2]}\nCategory: {books[2][3]}\nNumber: {books[2][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 250)
        Label(a_books, text = f"Id: {books[3][0]}\n{books[3][1]}\nAuthors: {books[3][2]}\nCategory: {books[3][3]}\nNumber: {books[3][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 570)
        Label(a_books, text = f"Id: {books[4][0]}\n{books[4][1]}\nAuthors: {books[4][2]}\nCategory: {books[4][3]}\nNumber: {books[4][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 570)
        Label(a_books, text = f"Id: {books[5][0]}\n{books[5][1]}\nAuthors: {books[5][2]}\nCategory: {books[5][3]}\nNumber: {books[5][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 570)

        Button(a_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red",command=lambda: self.short_history(n_books)).place(x = 15,y =330)
        Button(a_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
        Button(a_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
        Button(a_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
        Button(a_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
        Button(a_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

        img6 = ImageTk.PhotoImage(Image.open(books[0][-2]))
        Label(a_books,image=img6).place(x=40,y=80)

        img7 = ImageTk.PhotoImage(Image.open(books[1][-2]))
        Label(a_books,image=img7).place(x=260,y=80)

        img8 = ImageTk.PhotoImage(Image.open(books[2][-2]))
        Label(a_books,image=img8).place(x=490,y=80)

        img9 = ImageTk.PhotoImage(Image.open(books[3][-2]))
        Label(a_books,image=img9).place(x=40,y=365)

        img10 = ImageTk.PhotoImage(Image.open(books[4][-2]))
        Label(a_books,image=img10).place(x=260,y=365)

        img11 = ImageTk.PhotoImage(Image.open(books[5][-2]))
        Label(a_books,image=img11).place(x=490,y=365)

    def fantastic(self):
        global f_books
        global img12,img13,img14,img15,img16,img17
        f_books = Toplevel(self.category_screen)
        f_books.title("Fantastic_books")
        f_books.geometry("700x800+300+0")
        f_books["bg"] = "white" 
        # books = self.db.execute_and_return("select * from books where category = 'Fantasy'")
        books = self.db.get_books_by_category("Fantasy")
        print(books)
        Label(f_books,text = "FANTASY BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)

        Label(f_books, text = f"Id: {books[0][0]}\n{books[0][1]}\nAuthors: {books[0][2]}\nCategory: {books[0][3]}\nNumber: {books[0][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 250)
        Label(f_books, text = f"Id: {books[1][0]}\n{books[1][1]}\nAuthors: {books[1][2]}\nCategory: {books[1][3]}\nNumber: {books[1][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 250)
        Label(f_books, text = f"Id: {books[2][0]}\n{books[2][1]}\nAuthors: {books[2][2]}\nCategory: {books[2][3]}\nNumber: {books[2][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 250)
        Label(f_books, text = f"Id: {books[3][0]}\n{books[3][1]}\nAuthors: {books[3][2]}\nCategory: {books[3][3]}\nNumber: {books[3][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 570)
        Label(f_books, text = f"Id: {books[4][0]}\n{books[4][1]}\nAuthors: {books[4][2]}\nCategory: {books[4][3]}\nNumber: {books[4][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 570)
        Label(f_books, text = f"Id: {books[5][0]}\n{books[5][1]}\nAuthors: {books[5][2]}\nCategory: {books[5][3]}\nNumber: {books[5][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 570)

        Button(f_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red",command=lambda: self.short_history(n_books)).place(x = 15,y =330)
        Button(f_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
        Button(f_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
        Button(f_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
        Button(f_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
        Button(f_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

        img12 = ImageTk.PhotoImage(Image.open(books[0][-2]))
        Label(f_books,image=img12, text="fgjfghfghgfgfdfdrdthrd", compound=TOP).place(x=25,y=55)

        img13 = ImageTk.PhotoImage(Image.open(books[1][-2]))
        Label(f_books,image=img13).place(x=250,y=80)

        img14 = ImageTk.PhotoImage(Image.open(books[2][-2]))
        Label(f_books,image=img14).place(x=450,y=80)

        img15 = ImageTk.PhotoImage(Image.open(books[3][-2]))
        Label(f_books,image=img15).place(x=25,y=405)

        img16 = ImageTk.PhotoImage(Image.open(books[4][-2]))
        Label(f_books,image=img16).place(x=230,y=405)

        img17 = ImageTk.PhotoImage(Image.open(books[5][-2]))
        Label(f_books,image=img17).place(x=470,y=405)
    
    def business(self):
        global b_books
        global img18,img19,img20,img21,img22,img23
        b_books = Toplevel(self.category_screen)
        b_books.title("Business_books")
        b_books.geometry("700x800+300+0")
        b_books["bg"] = "white" 
        books = self.db.get_books_by_category("Business")
        print(books)

        Label(b_books,text = "BUSINESS BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)

        Label(b_books, text = f"Id: {books[0][0]}\n{books[0][1]}\nAuthors: {books[0][2]}\nCategory: {books[0][3]}\nNumber: {books[0][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 250)
        Label(b_books, text = f"Id: {books[1][0]}\n{books[1][1]}\nAuthors: {books[1][2]}\nCategory: {books[1][3]}\nNumber: {books[1][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 250)
        Label(b_books, text = f"Id: {books[2][0]}\n{books[2][1]}\nAuthors: {books[2][2]}\nCategory: {books[2][3]}\nNumber: {books[2][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 250)
        Label(b_books, text = f"Id: {books[3][0]}\n{books[3][1]}\nAuthors: {books[3][2]}\nCategory: {books[3][3]}\nNumber: {books[3][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 570)
        Label(b_books, text = f"Id: {books[4][0]}\n{books[4][1]}\nAuthors: {books[4][2]}\nCategory: {books[4][3]}\nNumber: {books[4][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 570)
        Label(b_books, text = f"Id: {books[5][0]}\n{books[5][1]}\nAuthors: {books[5][2]}\nCategory: {books[5][3]}\nNumber: {books[5][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 570)

        Button(b_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red",command=lambda: self.short_history(n_books)).place(x = 15,y =330)
        Button(b_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
        Button(b_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
        Button(b_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
        Button(b_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
        Button(b_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)
        
        img18 = ImageTk.PhotoImage(Image.open(books[0][-2]))
        Label(b_books,image=img18).place(x=40,y=90)

        img19 = ImageTk.PhotoImage(Image.open(books[1][-2]))
        Label(b_books,image=img19).place(x=260,y=90)

        img20 = ImageTk.PhotoImage(Image.open(books[2][-2]))
        Label(b_books,image=img20).place(x=490,y=75)

        img21 = ImageTk.PhotoImage(Image.open(books[3][-2]))
        Label(b_books,image=img21).place(x=30,y=375)

        img22 = ImageTk.PhotoImage(Image.open(books[4][-2]))
        Label(b_books,image=img22).place(x=260,y=385)

        img23 = ImageTk.PhotoImage(Image.open(books[5][-2]))
        Label(b_books,image=img23).place(x=490,y=385)

    def for_kids(self):
        global k_books
        global img24,img25,img26,img27,img28,img29
        k_books = Toplevel(self.category_screen)
        k_books.title("Business_books")
        k_books.geometry("700x800+300+0")
        k_books["bg"] = "white" 
        books = self.db.get_books_by_category("For kids")
        print(books)

        Label(k_books,text = "BOOKS FOR KIDS",font =("Times",20),bg = "white").place(x = 225,y=25)

        Label(k_books, text = f"Id: {books[0][0]}\n{books[0][1]}\nAuthors: {books[0][2]}\nCategory: {books[0][3]}\nNumber: {books[0][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 250)
        Label(k_books, text = f"Id: {books[1][0]}\n{books[1][1]}\nAuthors: {books[1][2]}\nCategory: {books[1][3]}\nNumber: {books[1][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 250)
        Label(k_books, text = f"Id: {books[2][0]}\n{books[2][1]}\nAuthors: {books[2][2]}\nCategory: {books[2][3]}\nNumber: {books[2][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 250)
        Label(k_books, text = f"Id: {books[3][0]}\n{books[3][1]}\nAuthors: {books[3][2]}\nCategory: {books[3][3]}\nNumber: {books[3][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 570)
        Label(k_books, text = f"Id: {books[4][0]}\n{books[4][1]}\nAuthors: {books[4][2]}\nCategory: {books[4][3]}\nNumber: {books[4][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 570)
        Label(k_books, text = f"Id: {books[5][0]}\n{books[5][1]}\nAuthors: {books[5][2]}\nCategory: {books[5][3]}\nNumber: {books[5][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 570)

        Button(k_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red",command=lambda: self.short_history(n_books)).place(x = 15,y =330)
        Button(k_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
        Button(k_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
        Button(k_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
        Button(k_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
        Button(k_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

        
        img24 = ImageTk.PhotoImage(Image.open("source\\img24.jpg"))
        Label(k_books,image=img24).place(x=30,y=100)

        img25 = ImageTk.PhotoImage(Image.open(books[1][-2]))
        Label(k_books,image=img25).place(x=260,y=110)

        img26 = ImageTk.PhotoImage(Image.open(books[2][-2]))
        Label(k_books,image=img26).place(x=490,y=130)

        img27 = ImageTk.PhotoImage(Image.open(books[3][-2]))
        Label(k_books,image=img27).place(x=30,y=430)

        img28 = ImageTk.PhotoImage(Image.open(books[4][-2]))
        Label(k_books,image=img28).place(x=260,y=450)

        img29 = ImageTk.PhotoImage(Image.open(books[5][-2]))
        Label(k_books,image=img29).place(x=490,y=430)

    def short_history(self, category_screen):
        global description, img8, text1
        description = Toplevel(category_screen)
        description.title("Description")
        description.geometry("500x700+300+0")
        text1 = Text(description)
        text1.insert(END, "A Brief History of Time plunges into the exotic realms of black holes and quarks, of antimatter and “arrows of time,” of the big bang and a bigger God—where the possibilities are wondrous and unexpected. With exciting images and profound imagination, Stephen Hawking brings us closer to the ultimate secrets at the very heart of creation")
        text1.pack()

    def psychologic(self):
        global p_books
        global img30,img31,img32,img33,img34,img35
        p_books = Toplevel(self.category_screen)
        p_books.title("Business_books")
        p_books.geometry("700x800+300+0")
        p_books["bg"] = "white" 
        books = self.db.get_books_by_category("Psychology")
        print(books)
        Label(p_books,text = "PSYCHOLOGY BOOKS",font =("Times",20),bg = "white").place(x = 225,y=25)

        Label(p_books, text = f"Id: {books[0][0]}\n{books[0][1]}\nAuthors: {books[0][2]}\nCategory: {books[0][3]}\nNumber: {books[0][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 250)
        Label(p_books, text = f"Id: {books[1][0]}\n{books[1][1]}\nAuthors: {books[1][2]}\nCategory: {books[1][3]}\nNumber: {books[1][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 250)
        Label(p_books, text = f"Id: {books[2][0]}\n{books[2][1]}\nAuthors: {books[2][2]}\nCategory: {books[2][3]}\nNumber: {books[2][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 250)
        Label(p_books, text = f"Id: {books[3][0]}\n{books[3][1]}\nAuthors: {books[3][2]}\nCategory: {books[3][3]}\nNumber: {books[3][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 570)
        Label(p_books, text = f"Id: {books[4][0]}\n{books[4][1]}\nAuthors: {books[4][2]}\nCategory: {books[4][3]}\nNumber: {books[4][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 570)
        Label(p_books, text = f"Id: {books[5][0]}\n{books[5][1]}\nAuthors: {books[5][2]}\nCategory: {books[5][3]}\nNumber: {books[5][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 570)

        Button(p_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red",command=lambda: self.short_history(n_books)).place(x = 15,y =330)
        Button(p_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
        Button(p_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
        Button(p_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
        Button(p_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
        Button(p_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)


        img30 = ImageTk.PhotoImage(Image.open(books[0][-2]))
        Label(p_books,image=img30).place(x=30,y=90)

        img31 = ImageTk.PhotoImage(Image.open(books[1][-2]))
        Label(p_books,image=img31).place(x=260,y=70)

        img32 = ImageTk.PhotoImage(Image.open(books[2][-2]))
        Label(p_books,image=img32).place(x=490,y=70)

        img33 = ImageTk.PhotoImage(Image.open(books[3][-2]))
        Label(p_books,image=img33).place(x=30,y=380)

        img34 = ImageTk.PhotoImage(Image.open(books[4][-2]))
        Label(p_books,image=img34).place(x=250,y=380)

        img35 = ImageTk.PhotoImage(Image.open(books[5][-2]))
        Label(p_books,image=img35).place(x=490,y=380)

    def novels(self):
        global n_books
        global img36,img37,img38,img39,img40,img41
        n_books = Toplevel(self.category_screen)
        n_books.title("Novels")
        n_books.geometry("700x800+300+0")
        n_books["bg"] = "white" 
        Label(n_books,text = "NOVELS",font =("Times",20),bg = "white").place(x = 250,y=15)
        books = self.db.get_books_by_category("Novel")
        print(books)


        Label(n_books, text = f"Id: {books[0][0]}\n{books[0][1]}\nAuthors: {books[0][2]}\nCategory: {books[0][3]}\nNumber: {books[0][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 250)
        Label(n_books, text = f"Id: {books[1][0]}\n{books[1][1]}\nAuthors: {books[1][2]}\nCategory: {books[1][3]}\nNumber: {books[1][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 250)
        Label(n_books, text = f"Id: {books[2][0]}\n{books[2][1]}\nAuthors: {books[2][2]}\nCategory: {books[2][3]}\nNumber: {books[2][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 250)
        Label(n_books, text = f"Id: {books[3][0]}\n{books[3][1]}\nAuthors: {books[3][2]}\nCategory: {books[3][3]}\nNumber: {books[3][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 15, y = 570)
        Label(n_books, text = f"Id: {books[4][0]}\n{books[4][1]}\nAuthors: {books[4][2]}\nCategory: {books[4][3]}\nNumber: {books[4][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 240, y = 570)
        Label(n_books, text = f"Id: {books[5][0]}\n{books[5][1]}\nAuthors: {books[5][2]}\nCategory: {books[5][3]}\nNumber: {books[5][4]}", font = ("Times",10),bg = "light sky blue",fg = "black").place(x = 480, y = 570)

        Button(n_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red",command=lambda: self.short_history(n_books)).place(x = 15,y =330)
        Button(n_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =330)
        Button(n_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =330)
        Button(n_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 15,y =650)
        Button(n_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 240,y =650)
        Button(n_books,text = "Choose",font = ("Times",8),bg = "white",fg = "red").place(x = 480,y =650)

        
        img36 = ImageTk.PhotoImage(Image.open(books[0][-2]))
        Label(n_books,image=img36).place(x=25,y=60)

        img37 = ImageTk.PhotoImage(Image.open(books[1][-2]))
        Label(n_books,image=img37).place(x=240,y=60)

        img38 = ImageTk.PhotoImage(Image.open(books[2][-2]))
        Label(n_books,image=img38).place(x=490,y=60)

        img39 = ImageTk.PhotoImage(Image.open(books[3][-2]))
        Label(n_books,image=img39).place(x=25,y=380)

        img40 = ImageTk.PhotoImage(Image.open(books[4][-2]))
        Label(n_books,image=img40).place(x=240,y=380)

        img41 = ImageTk.PhotoImage(Image.open(books[5][-2]))
        Label(n_books,image=img41).place(x=490,y=380)