import mysql.connector as connector
connection=connector.connect(user="mario",password="cuisine")

# Creating cursor object
cursor = connection.cursor()

# Setting the database for the use
cursor.execute("USE little_lemon")

# Task 1
#SELECT GuestFirstName, GuestLastName,

# The SQL query is:
sql_query="""
SELECT 
BookingID AS ID,
UPPER(CONCAT(GuestFirstName,' ',GuestLastName)) 
AS GuestFullName 
FROM bookings;"""

# Execute query
cursor.execute(sql_query)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Just add an empty line using print statement
print()

# Print query results
for result in results:
    print(result)  

# Task 2

# The SQL query is:
sql_query="""
SELECT 
COUNT(BookingID) AS n_bookings,
SUM(BillAmount) AS Total_sale,
AVG(BillAmount) AS Avg_sale
FROM Orders;"""

# Execute query
cursor.execute(sql_query)

# Fetch records
results=cursor.fetchall()

# Print results
print("Today's statistics:")
for result in results:
    print("Number of bookings:",result[0])
    print("Total sale:",result[1])
    print("Average sale:",result[2])


# Task 3

# The SQL query is:
sql_query="""SELECT 
TableNo AS 'Table number', 
COUNT(TableNo) AS n_booking
FROM Bookings 
GROUP BY TableNo 
ORDER BY n_booking DESC;"""

# Execute query
cursor.execute(sql_query)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)


# Task 4

# The SQL query is:
sql_query="""
SELECT
BookingID,
CONCAT(GuestFirstName,' ',GuestLastName) AS Guest_Name,

CASE
WHEN HOUR(BookingSlot) IN (15,16) THEN "Late afternoon" 
WHEN HOUR(BookingSlot) IN (17,18) THEN "Evening" 
WHEN HOUR(BookingSlot) IN (19,20) THEN "Night"
ELSE "Time not available" 
END AS Arrival_slot

FROM Bookings;"""

# Execute query
cursor.execute(sql_query)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)


# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")