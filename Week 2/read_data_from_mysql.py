import mysql.connector as connector

connection = connector.connect(user = "mario", password = "cuisine")
cursor = connection.cursor()

cursor.execute("USE little_lemon")

# my_sql_insert_query = """
# INSERT INTO bookings
# (GuestFirstName, GuestLastName, TableNo, BookingSlot, EmployeeID)
# VALUES
# ('Marcos', 'Romero', '2', '19:00', 5)
# """

# cursor.execute(my_sql_insert_query)
# connection.commit()

read_data_query = """SELECT * FROM bookings"""

cursor.execute(read_data_query)
result = cursor.fetchall()

print(result)

columns = cursor.column_names



