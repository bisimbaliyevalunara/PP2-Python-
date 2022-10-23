#import modules
from tkinter import *
import tkinter as tk 
import os
from PIL import ImageTk, Image
from tkinter import messagebox
 
# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text = "Please enter details below", font = ("Times",14)).pack(padx = 5,pady = 15)

    username_lable = Label(register_screen, text = "New username",font = ("Times",11)).place(x = 20,y = 64)
    Label(register_screen, text = "").pack()
    Entry(register_screen, textvariable = username).place(x = 120,y = 70)

    Label(register_screen, text = "New password",font = ("Times",11)).place(x = 20,y = 105)
    Label(register_screen, text = "").pack()
    Entry(register_screen, textvariable = password, show='*').place(x = 120,y = 105)

    rad3 = Radiobutton(register_screen, text='Student', value=1).place(x = 50,y = 150)
    rad4 = Radiobutton(register_screen, text='Professor', value=2).place(x = 150,y = 150)
    

    Button(register_screen, text = "Register", width = 10, height = 1, command = register_user).place(x = 98,y = 188)

 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text = "Please enter details below to login", font = ("Times",13)).pack(padx = 10,pady = 10)

 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text = "Username",font = ("Times",11)).place(x = 20,y = 65)
    Label(login_screen, text = "").pack()
    username_login_entry = Entry(login_screen, textvariable = username_verify)
    username_login_entry.pack()
    
    Label(login_screen, text = "Password",font= ("Times",11)).place(x = 20, y = 105 )
    Label(login_screen, text = "").pack()
    password_login_entry = Entry(login_screen, textvariable = password_verify, show= '*')
    password_login_entry.pack()
    
    
    rad1 = Radiobutton(login_screen, text='Student', value=1).place(x = 168,y = 148)
    rad2 = Radiobutton(login_screen, text='Professor', value=2).place(x = 58,y = 148)
    

    Button(login_screen, text = "Login", width = 10, height = 1, command = login_verify).place(x = 100,y = 190)

 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text = "Registration Success", fg = "green", font = ("Times", 11)).pack()
    

# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_succsess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_succsess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Library")
    login_success_screen.geometry("350x350")
    Label(login_success_screen, text = "Cotigories Book").pack()
    Button(login_success_screen, text = "OK", command = delete_login_success).pack()



# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text = "Invalid Password ").pack()
    Button(password_not_recog_screen, text = "OK", command = delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text = "User Not Found").pack()
    Button(user_not_found_screen, text = "OK", command = delete_user_not_found_screen).pack()
 
# Deleting popups
 

def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
main_screen = Tk()
main_screen.geometry("300x250")
main_screen.title("Account Login")
path = 'source\\welcome.jpg'
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(main_screen, image = img)
panel.place(x=0, y=0, relwidth=1, relheight=1)

Button(text = "Login",font = ("Times" ,13),command = login).place(x = 120,y = 70)
Label(text = "").pack()
Button(text = "Register",font = ("Times" ,13),command = register).place(x = 110, y =130)




 
main_screen.mainloop()
 
