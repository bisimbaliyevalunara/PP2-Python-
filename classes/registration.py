from tkinter import *
from PIL import ImageTk, Image

class Registration:
    def __init__(self, db):
        self.db = db
        # self.db = Database()
        # self.root = root  # Tk object main window
        
    def start(self):
        self.root = Tk()
        self.root.geometry("300x250")
        self.root.title("Account Login")
        self.root.resizable(False, False)
        self.state = False
        image = ImageTk.PhotoImage(Image.open("source\\welcome.jpg"))
        Label(self.root, image = image).place(x = 0, y = 0, relwidth = 1, relheight = 1)
        Button(text = "Exit", font = ("Times", 13), command = self.root.destroy).place(x = 250, y = 0)
        Button(text = "Login", font = ("Times", 13), command = self.login).place(x = 120, y = 70)
        Button(text = "Register", font = ("Times", 13), command = self.register).place(x = 110, y = 130)

        self.root.mainloop()

    def register(self):
        global register_screen
        register_screen = Toplevel(self.root)
        register_screen.title("Register")
        register_screen.geometry("400x350")
        register_screen.resizable(False, False)
    
        global username, password, role
        global username_entry, password_entry
        global first_name_entry, last_name_entry
    
        username = StringVar(); password = StringVar(); role = StringVar()
    
        Button(register_screen, text = "Back", command = register_screen.destroy).place(x = 360, y = 5)
        Label(register_screen, text = "Please enter details below", font = 20).pack()
        Label(register_screen, text = "").pack()
        first_name = Label(register_screen, text = "First name"); first_name.pack()
        first_name_entry = Entry(register_screen); first_name_entry.pack()
        last_name = Label(register_screen, text = "Last name"); last_name.pack()
        last_name_entry = Entry(register_screen); last_name_entry.pack()
        login_table = Label(register_screen, text = "Username")
        login_table.pack()
        username_entry = Entry(register_screen, textvariable = username); username_entry.pack()
        password_lable = Label(register_screen, text = "Password * "); password_lable.pack()
        password_entry = Entry(register_screen, textvariable = password, show='*'); password_entry.pack()
        role.set("None")
        Label(register_screen, text = "").pack()
        radiobuttonframe = Frame(register_screen); radiobuttonframe.pack()
        R1 = Radiobutton(radiobuttonframe, text = "student", variable = role, value = "student"); R1.pack(side = LEFT)
        R2 = Radiobutton(radiobuttonframe, text = "professor", variable = role, value = "professor"); R2.pack(side = LEFT)

        Label(register_screen, text = "").pack()
        Button(register_screen, text = "Register", width = 10, height = 1, command = self.register_user).pack()
    
    def login(self):
        global login_screen
        login_screen = Toplevel(self.root)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        login_screen.resizable(False, False)
        Button(login_screen, text = "Back", command = login_screen.destroy).place(x = 260, y = 5)
        Label(login_screen, text = "Please enter details below to login").pack()
        Label(login_screen, text = "").pack()
    
        global username_verify
        global password_verify
    
        username_verify = StringVar()
        password_verify = StringVar()
    
        global username_login_entry
        global password_login_entry
    
        Label(login_screen, text = "Username").pack()
        username_login_entry = Entry(login_screen, textvariable = username_verify); username_login_entry.pack()
        Label(login_screen, text = "").pack()
        Label(login_screen, text = "Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable = password_verify, show= '*'); password_login_entry.pack()
        Label(login_screen, text = "").pack()
        Button(login_screen, text = "Login", width = 10, height = 1, command = self.login_verify).pack()
    
    def register_user(self):
        first_name_info = first_name_entry.get()
        last_name_info = last_name_entry.get()
        username_info = username.get()
        password_info = password.get()
        role_info = role.get()
        values = (first_name_info, last_name_info, username_info, password_info, role_info)

        if len(first_name_info) and len(last_name_info) and len(username_info) and len(password_info) and len(role_info):
            if self.db.insert_user(values): 
                self.register_success()
                # get new user id
                self.user = username_info
                print(f"\nnew user\nlogin: {username_info}\npassword: {password_info}\n")
                self.state = True
                # Label(register_screen, text = "Registration Success", fg = "green", font = ("calibri", 11)).pack()
            else: 
                self.user_not_registered()
                # Label(register_screen, text = "Error", fg = "red", font = ("calibri", 11)).pack()
        else:
            self.user_not_registered()
            # Label(register_screen, text = "Incorrect data", fg = "red", font = ("calibri", 11)).pack()
        print(self.state)

        first_name_entry.delete(0, END); last_name_entry.delete(0, END)
        username_entry.delete(0, END); password_entry.delete(0, END)
        role.set("None")
        
    def login_verify(self):
        username1 = username_verify.get(); password1 = password_verify.get()
        username_login_entry.delete(0, END); password_login_entry.delete(0, END)

        if self.db.check_login(username1):
            if self.db.check_password(password1):
                self.login_success()
                # get user id by login
                self.user = username1
                print(f"\nuser\nlogin: {username1}\npassword: {password1}\n")
                self.state = True
            else:
                self.password_not_recognised()
        else: 
            self.user_not_found()
        print(self.state)
    
    def login_success(self):
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        login_success_screen.resizable(False, False)
        Label(login_success_screen, text = "Login Success").pack()
        Button(login_success_screen, text = "OK", command = self.delete_login_success).pack()

    def register_success(self):
        global register_success_screen
        register_success_screen = Toplevel(register_screen)
        register_success_screen.title("Success")
        register_success_screen.geometry("150x100")
        register_success_screen.resizable(False, False)
        Label(register_success_screen, text = "Register Success").pack()
        Button(register_success_screen, text = "OK", command = self.delete_register_success).pack()

    def user_not_registered(self):
        global user_not_registered_screen
        user_not_registered_screen = Toplevel(register_screen)
        user_not_registered_screen.title("Success")
        user_not_registered_screen.geometry("150x100")
        user_not_registered_screen.resizable(False, False)
        Label(user_not_registered_screen, text = "User not registered! ").pack()
        Button(user_not_registered_screen, text = "OK", command = self.delete_user_not_registered_screen).pack()

    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        password_not_recog_screen.resizable(False, False)
        Label(password_not_recog_screen, text = "Invalid Password ").pack()
        Button(password_not_recog_screen, text = "OK", command = self.delete_password_not_recognised).pack()
    
    def user_not_found(self):
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        user_not_found_screen.resizable(False, False)
        Label(user_not_found_screen, text = "User Not Found").pack()
        Button(user_not_found_screen, text = "OK", command = self.delete_user_not_found_screen).pack()
    
    def delete_login_success(self):
        login_success_screen.destroy(); login_screen.destroy(); self.root.destroy()

    def delete_register_success(self):
        register_success_screen.destroy(); register_screen.destroy(); self.root.destroy() 
    
    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()
      
    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()

    def delete_user_not_registered_screen(self):
        user_not_registered_screen.destroy()
