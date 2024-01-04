import mysql.connector as connector

connection = connector.connect(user = "mario", password = "cuisine")
cursor = connection.cursor()

use_database_query = """USE little_lemon"""

cursor.execute(use_database_query)
print(connection.database)

stored_procedure_query = """
CREATE PROCEDURE GetCustomersAndBillAmount()
BEGIN
SELECT bookings.BookingID,
CONCAT(bookings.GuestFirstName, ' ' , bookings.GuestLastName) AS CustomerName,
Orders.BillAmount
FROM bookings
INNER JOIN
Orders ON bookings.BookingID = Orders.BookingID
WHERE BillAmount >= 50
ORDER BY BillAmount DESC;
END 
"""

cursor.execute(stored_procedure_query)


cursor.callproc("GetCustomersAndBillAmount")

results = next(cursor.stored_results())

dataset = results.fetchall()

for data in dataset:
    print(data)
