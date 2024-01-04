import mysql.connector as connector
import datetime as dt

connection = connector.connect(user = "mario", password ="cuisine")
cursor = connection.cursor()

cursor.execute("USE little_lemon")

select_stmt = """SELECT * FROM bookings"""

cursor.execute(select_stmt)

print(cursor.column_names)

for row in cursor:
    booking_id = row[0]
    booking_slot = row[4] 
    new_booking_slot = booking_slot + dt.timedelta(hours = 1)
    print("booking id {} is moved from {} to {}".format(booking_id, booking_slot, new_booking_slot))
