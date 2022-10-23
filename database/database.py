from database.config import config
class Database():    
    def __init__(self):
        self.db = config()
        self.cursor = self.db.cursor()
        self.cursor.execute("create database if not exists library")
        self.cursor.execute("use library")
        # self.create_tables()
        # self.insert_books()
        # self.insert_users()
        # self.insert_borrowed_books()

    def fill_database(self):
        self.insert_books()
        self.insert_users()


    def create_tables(self):
        tables = [
            """
            create table if not exists books (
                book_id int auto_increment primary key, name varchar(255) not null,
                author varchar(255) not null, category varchar(255) not null, 
                number int not null, image varchar(255) not null, description text not null
            )
            """,
            # role is student or professor
            # status to check fine
            """
            create table if not exists users (
                user_id int auto_increment primary key, first_name varchar(255) not null, 
                last_name varchar(255) not null, login varchar(255) unique not null, password varchar(255) not null, 
                role varchar(255) not null
            )
            
            """,
            """
            create table if not exists borrowed_books (
                borrow_id int auto_increment primary key, 
                book_id int not null, user_id int not null, 
                borrowed_date date not null, returned_date date default '2022/12/31',
                foreign key (book_id) references books(book_id),
                foreign key (user_id) references users(user_id) 
            )
            """, 
            """
            create table if not exists black_list (
                id int auto_increment primary key,
                user_id int not null,
                foreign key (user_id) references users (user_id)   
            )
            """
        ]
        [self.cursor.execute(table) for table in tables]
        self.db.commit()

    def delete_table(self, table):
        try: 
            self.cursor.execute(f"drop table if exists {table}")
            print(f"the table {table} succesfully deleted")
            self.db.commit()
        except: print(f"the table {table} not deleted!")
    
    def delete_all_tables(self):
        try:
            # tables = self.show_tables()
            # [self.delete_table(table[0]) for table in tables]
            self.delete_table("black_list")
            self.delete_table("borrowed_books")
            self.delete_table("users")
            self.delete_table("books")
            print("All tables was deleted")
            self.db.commit()
        except: print("Tables not deleted!")
        
    def show_tables(self):
        self.cursor.execute("show tables")
        return self.cursor.fetchall()

    def get_table_data(self, table):
        self.cursor.execute(f"select * from {table}")
        return self.cursor.fetchall()

    def get_user_by_login(self, login):
        self.cursor.execute(f"select * from users where login = '{login}'")
        return self.cursor.fetchall()

    def get_books_by_category(self, category):
        self.cursor.execute(f"select * from books where category = '{category}'")
        return self.cursor.fetchall()

    def check_amount_of_book(self, book_id, number):
        query = f"select * from books where book_id = {book_id} and number >= {number}"
        self.cursor.execute(query)
        return len(self.cursor.fetchall())

    def update_amount_of_book(self, book_id, number):
        query = f"update books set number = number - {number} where book_id = {book_id}"
        self.cursor.execute(query)
        self.db.commit()
        print(f"The book with id = {book_id} succesfully updated")
        return True

    def update_and_check_amount_of_book(self, book_id, number):
        query = f"update books set number = number - {number} where book_id = {book_id} and number >= {number}"
        self.cursor.execute(query)
        self.cursor.execute(f"select * from books where book_id = {book_id}")
        self.db.commit()
        print(f"The book with id = {book_id} succesfully updated")
        # return len(self.cursor.fetchall())

    def insert_books(self):
        try:
            books = open("tables\\books.txt").read().split("\n")
            query = "insert into books (name, author, category, number, image, description) values (%s, %s, %s, %s, %s, %s)"
            [self.cursor.execute(query, tuple(book.split(";"))) for book in books]
            self.db.commit()
            print("the books succesfully inserted")
            return True
        except:
            print("the books not inserted!")
            return False

    def insert_users(self):
        try:
            users = open("tables\\users.txt").read().split("\n")
            # print(users)
            query = "insert into users (first_name, last_name, login, password, role) values (%s, %s, %s, %s, %s)"                
            [self.cursor.execute(query, tuple(user.split(";"))) for user in users]
            print("the users succesfully inserted")
            self.db.commit()
            return True
        except:
            print("the users not inserted!")
            return False

    def insert_borrowed_books(self):
        try:
            borrowed_books = open("tables\\borrowed_books.txt").read().split("\n")
            query = "insert into borrowed_books (book_id, user_id, borrowed_date, returned_date) values (%s, %s, %s, %s)"
            [self.cursor.execute(query, tuple(borrowed_book.split(";"))) for borrowed_book in borrowed_books]
            print("the borrowed books succesfully inserted")
            self.db.commit()
            return True
        except:
            print("the borrowed books not inserted!")
            return False

    def insert_user(self, values):
        try:
            query = "insert into users (first_name, last_name, login, password, role) values (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, values)
            self.db.commit()
            print("the user successfully inserted")
            return True
        except: 
            print("the user not inserted!")
            return False

    def show_history(self, login):
        # query = "select book_id, user_id where (returned_date - borrowed_date) > 30"
        query = "select user_id from users where login = %s"
        self.cursor.execute(query, (login, ))
        # book_id, user_id = self.cursor.fetchall()

        # query2 = """select users.first_name, users.last_name, books.name, books.author from users, books 
        # where users.user_id = %s and books.book_id = %s"""
        query2 = ""
        # self.cursor.execute(query2, (user_id, book_id))
        pass

    def execute_and_return(self, query):
        self.cursor.execute(f"{query}")
        return self.cursor.fetchall()
        

    def clear_table(self, table):
        self.cursor.execute(f"delete from {table}")
        self.db.commit()
        
    def check_password(self, password):
        self.cursor.execute("select password from users where password = %s", (password, ))
        return len(self.cursor.fetchall())

    def check_login(self, login):
        self.cursor.execute("select login from users where login = %s", (login, ))
        return len(self.cursor.fetchall())

