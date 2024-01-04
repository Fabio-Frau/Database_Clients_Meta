import mysql.connector as connector
import datetime as dt

connection = connector.connect(user = "mario", password ="cuisine")
cursor = connection.cursor()

cursor.execute("USE little_lemon")

sql_query = """SELECT SUM(BillAmount) AS Total_Sale FROM Orders;"""

cursor.execute(sql_query)

results = cursor.fetchall()
for result in results:
    print(result)


sql_query = """SELECT HOUR(BookingSlot) FROM Bookings;"""
cursor.execute(sql_query)
results = cursor.fetchall()
for result in results:
    print(result)
