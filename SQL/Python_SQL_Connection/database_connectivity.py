import mysql.connector as c
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "retail"
)
print("Connected to Database")
mycursor = mydb.cursor()

#id = input("Enter your id")
#name = input("Enter your name")
mycursor.execute("SELECT * FROM stu")
students = mycursor.fetchall()
for std in students:
    print(std)
#mydb.commit()
