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
mycursor.execute("DELETE FROM company WHERE id = %s ", (id,))
print("ROW DELETED")
mydb.commit()

"""
OUTPUT:
DELETED COMPANY WHOSE ID = 292

mysql> select *from company;
+------+-----------+------------+------+
| id   | name      | place      | rank |
+------+-----------+------------+------+
|  101 | Bitlabs   | Vijayawada |    1 |
| 1024 | Google    | Hyderabad  |    3 |
|  112 | Microsoft | Banglore   |    7 |
|  432 | Amazon    | Delhi      |    9 |
|  532 | TCS       | Hyderabad  |   49 |
+------+-----------+------------+------+
5 rows in set (0.00 sec)


"""