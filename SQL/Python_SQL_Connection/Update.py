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
rank = input("Enter company rank : ")
mycursor.execute("UPDATE company SET rank = %s WHERE id = %s", (rank, id,))
print("ROW UPDATED")
mydb.commit()

"""
OUTPUT:
UPDATED RANK OF COMPANY WITH id = 432 TO rank = 5

mysql> select *from company;
+------+-----------+------------+------+
| id   | name      | place      | rank |
+------+-----------+------------+------+
|  101 | Bitlabs   | Vijayawada |    1 |
| 1024 | Google    | Hyderabad  |    3 |
|  112 | Microsoft | Banglore   |    7 |
|  432 | Amazon    | Delhi      |    5 |
|  532 | TCS       | Hyderabad  |   49 |
+------+-----------+------------+------+
5 rows in set (0.00 sec)


"""