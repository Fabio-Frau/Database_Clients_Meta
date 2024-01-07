from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error
import mysql.connector as connector


dbconfig = {
    "database":"little_lemon_db",
    "user" : "mario",
    "password" : "cuisine"
}

try:
    pool = MySQLConnectionPool(pool_name = "pool_a",
                           pool_size = 2, #default is 5
                           **dbconfig)
    print("The connection pool is created with a name: ",pool.pool_name)
    print("The pool size is:",pool.pool_size)

except Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)


print("Getting a connection from the pool.")
connection1 = pool.get_connection()

print("A user with connection id {} is connected to the database.".format(
    connection1.connection_id))

db_Info = connection1.get_server_info()
print("MySQL server version is:", db_Info)

print("Creating a cursor object.")
cursor = connection1.cursor()

#Task 2

query_peak_hours = """
CREATE PROCEDURE PeakHours()
BEGIN
SELECT
HOUR(BookingSlot) AS `booking hour`,
COUNT(HOUR(BookingSlot)) AS `number of bookings`
FROM bookings
GROUP BY `booking hour`
ORDER BY `number of bookings` DESC;
END
"""

cursor.execute(query_peak_hours)

cursor.callproc("PeakHours")

results = next( cursor.stored_results() )
dataset = results.fetchall()

for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

print(columns)

for data in dataset:
    print(data)


#Task 3

query_guest_status ="""
CREATE PROCEDURE GuestStatus()
BEGIN
SELECT
CONCAT(bookings.GuestFirstName, ' ', bookings.GuestLastName) AS GuestFullName,
CASE
WHEN employees.Role IN ("Manager", "Assistant Manager") THEN "Ready to pay"
WHEN employees.Role = "Head Chef" THEN "Ready to serve"
WHEN employees.Role = "Assistant Chef" THEN "Preparing Order"
WHEN employees.Role = "Head Waiter" THEN "Order served"
END AS "Status"
FROM bookings
LEFT JOIN employees ON bookings.EmployeeID = employees.EmployeeID;
END
"""

cursor.execute(query_guest_status)

cursor.callproc("GuestStatus")

results = next( cursor.stored_results() )
dataset = results.fetchall()

for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

print(columns)

for data in dataset:
    print(data)


connection1.close()


