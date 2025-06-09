import mysql.connector as c
mydb = c.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "company"
)
print("Connected to Database")
mycursor = mydb.cursor()

id = input("Enter company id : ")
name = input("Enter company name : ")
place = input("Enter company place : ")
rank = input("Enter company rank : ")
mycursor.execute("INSERT INTO company VALUES(%s, %s, %s, %s)", (id, name, place, rank))
print("ROW INSERTED")
mydb.commit()

"""
OUTPUT: 

mysql> select *from company;
+------+-----------+------------+------+
| id   | name      | place      | rank |
+------+-----------+------------+------+
|  101 | Bitlabs   | Vijayawada |    1 |
| 1024 | Google    | Hyderabad  |    3 |
|  112 | Microsoft | Banglore   |    7 |
|  432 | Amazon    | Delhi      |    9 |
|  292 | Flipkart  | Hyderabad  |   55 |
|  532 | TCS       | Hyderabad  |   49 |
+------+-----------+------------+------+
6 rows in set (0.00 sec)


"""
