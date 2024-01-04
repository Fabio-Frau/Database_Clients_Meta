import mysql.connector as connector
import datetime as dt

# Establish connection between Python and MySQL database via MySQL Connector/Python API
connection=connector.connect(user="mario", password="cuisine" )

# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()

# Set the little_lemon database for use 
cursor.execute("use little_lemon")

# Confirm the datbase in use
connection.database

# Read query 
#all_bookings = """SELECT GuestFirstName, GuestLastName, 
#TableNo FROM bookings;"""


# The SQL query is:
sql_query = """SELECT 
COUNT(BookingID) AS n_bookings,
HOUR(BookingSlot) AS Hour 
FROM Bookings
GROUP BY Hour
ORDER BY Hour ASC;"""

# Execute the query 
cursor.execute(sql_query)

# Fetch all results that satisfy the query 
results = cursor.fetchall()

# Print records in the required format using for loop
print("""Upcoming Bookings:\n""")
#print(cols)
for result in results:
    print("Hour: ",result[1],"<<>>", result[0], "Booking/s")


# The SQL query is: 
sql_query = """SELECT 
TableNo, 
GuestFirstName, 
GuestLastName, 
BookingSlot 
FROM Bookings 
ORDER BY BookingSlot;"""

# Execute query 
cursor.execute(sql_query)

# Fetch all results that satisfy the query 
results = cursor.fetchall()

# Print records in the required format
print("The guests and their booking slots are:\n")
for result in results: 
    time = str(result[3])
    hour = dt.datetime.strptime(time,'%H:%M:%S').hour
    minute = dt.datetime.strptime(time,'%H:%M:%S').minute
    print("[Table no:]",result[0],">>",result[1],result[2], "is expected to arrive at:", 
          hour,"hrs and", minute, "mins")
    



"""UPDATE Bookings 
SET BookingSlot=ADDTIME(BookingSlot,"1:00:00") 
WHERE BookingID=2;"""

# The SQL query is: 
sql_query = """SELECT 
BookingID, 
TableNo, 
BookingSlot, 
ADDTIME(BookingSlot,"1:00:00") as NewTime 
FROM Bookings
WHERE TableNo = 12 AND BookingID = 2;"""

# Execute query 
cursor.execute(sql_query)

# Fetch all results that satisfy the query 
results = cursor.fetchall()

# Print time change alert.
print("Booking time change ALERT!!")
for result in results:  
    print("Booking ID:",result[0])
    print("Table number:",result[1])
    print("Booked slot:",result[2])
    print("New arrival time:",result[3])