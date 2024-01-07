from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error
import mysql.connector as connector
import datetime as dt


dbconfig = {
    "database":"little_lemon_db",
    "user" : "mario",
    "password" : "cuisine"
}

try:
    pool = MySQLConnectionPool(pool_name = "pool_b",
                           pool_size = 32, #default is 5
                           **dbconfig)
    print("The connection pool is created with a name: ",pool.pool_name)
    print("The pool size is:",pool.pool_size)

except Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)


bookings = {"Guest1" : {"Table number" : 8, "First Name" :"Aneas", "Last Name" : "Java", "Booking Time" : dt.time(18,0), "EmployeeID" : 6},
            "Guest2" : {"Table number" : 5, "First Name" :"Bald", "Last Name" : "Vin", "Booking Time" : dt.time(19,0), "EmployeeID" : 6},
            "Guest3" : {"Table number" : 12, "First Name" :"Jay", "Last Name" : "Kon", "Booking Time" : dt.time(19,30), "EmployeeID" : 6}}



for guestID, guest  in bookings.items():
    try:
        guest_connected = pool.get_connection()
        
        print("[{}] is connected.\n".format(guestID))
        insert_query = """INSERT INTO bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES ({},'{}','{}','{}',{});""".format(guest["Table number"], guest["First Name"], guest["Last Name"], guest["Booking Time"], guest["EmployeeID"])             
        print(insert_query)

        cursor = guest_connected.cursor()
        cursor.execute(insert_query)
        guest_connected.commit()        

    except:
        print("No more connections are available.")
        print("Adding new connection in the pool.")





        

        

   
