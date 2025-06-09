import mysql.connector as c
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "company"
)
print("Connected to Database")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM company")
companies = mycursor.fetchall()
for com in companies:
    print(com)

"""
OUTPUT:

Connected to Database
(101, 'Bitlabs', 'Vijayawada', 1)
(1024, 'Google', 'Hyderabad', 3)
(112, 'Microsoft', 'Banglore', 7)
(432, 'Amazon', 'Delhi', 5)
(532, 'TCS', 'Hyderabad', 49)

Process finished with exit code 0

"""

print()
print()
print("COMPANY NAMES IN ASCENDING ORDER")
mycursor.execute("SELECT * FROM company ORDER BY name ASC")
companies = mycursor.fetchall()
for com in companies:
    print(com)

"""
OUTPUT:

COMPANY NAMES IN ASCENDING ORDER
(432, 'Amazon', 'Delhi', 5)
(101, 'Bitlabs', 'Vijayawada', 1)
(1024, 'Google', 'Hyderabad', 3)
(112, 'Microsoft', 'Banglore', 7)
(532, 'TCS', 'Hyderabad', 49)

Process finished with exit code 0

"""

print()
print()
print("COMPANY RANK BETWEEN 1-10")
mycursor.execute("SELECT * FROM company WHERE rank BETWEEN 1 and 10")
companies = mycursor.fetchall()
for com in companies:
    print(com)

"""
OUTPUT:

COMPANY RANK BETWEEN 1-10
(101, 'Bitlabs', 'Vijayawada', 1)
(1024, 'Google', 'Hyderabad', 3)
(112, 'Microsoft', 'Banglore', 7)
(432, 'Amazon', 'Delhi', 5)

Process finished with exit code 0

"""

print()
print()
print("COMPANIES IN HYDERABAD")
mycursor.execute("SELECT * FROM company WHERE place = 'Hyderabad'")
companies = mycursor.fetchall()
for com in companies:
    print(com)

"""
OUTPUT:

COMPANIES IN HYDERABAD
(1024, 'Google', 'Hyderabad', 3)
(532, 'TCS', 'Hyderabad', 49)

Process finished with exit code 0
"""