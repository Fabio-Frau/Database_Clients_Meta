import mysql.connector as connector
from mysql.connector.pooling import MySQLConnectionPool


connection = connector.connect(user = "mario", password="cuisine")
cursor = connection.cursor()
cursor.execute("USE little_lemon")

pool = MySQLConnectionPool(pool_name = "little_lemon_pool",
                           pool_size=4,
                           host = "localhost",
                           database = "little_lemon",
                           user = "mario",
                           password = "cuisine")

users = ["mary", "john", "michael", "tony"]

select_stmt = "SELECT * FROM bookings WHERE BookingID=%(booking_id)s"

for i in range(pool.pool_size):
    conn = pool.get_connection()
    if conn.is_connected:
        cursor = conn.cursor()
        print("The connection id for {} {} is requesting info on booking {}"
              .format(users[i], conn.connection_id, i+1))
        cursor.execute(select_stmt, {'booking_id': i + 1})
        print(cursor.fetchall())
    else:
        print("no live connection made")
    conn.close()