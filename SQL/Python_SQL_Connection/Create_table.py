import mysql.connector as c
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "company"
)
print("Connected to Database")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE company (id int, name varchar(20), place varchar(50), rank int)")
print("TABLE CREATED")
mydb.commit()

