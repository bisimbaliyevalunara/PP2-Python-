import mysql.connector as mysql
def config():
    db = mysql.connect(
        host = "localhost",
        user = "root",
        password = "Lunara.2003"
    )
    return db