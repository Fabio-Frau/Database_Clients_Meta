import mysql.connector as connector

my_sql_query ="""
SELECT BookingID, BillAmount
FROM Orders
WHERE BillAmount >= 40
ORDER BY BillAmount ASC
"""

connection = connector.connect(user ="mario", password = "cuisine")

cursor = connection.cursor()
cursor.execute("USE little_lemon")
cursor.execute(my_sql_query)

results = cursor.fetchall()

for result in results:
    print(result)