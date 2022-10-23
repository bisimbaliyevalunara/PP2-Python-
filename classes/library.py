from classes.registration import Registration
from classes.category import Category
from database.database import Database

class LibraryManagmentSystem:
    def __init__(self):
        self.db = Database()

    def start(self):
        self.register = Registration(self.db)
        self.register.start()
        while True:
            if self.register.state:
                self.category = Category(self.db, self.register.user); self.category.start()
                if self.category.state:
                    self.register = Registration(self.db); self.register.start()
                else: break
            else: break
