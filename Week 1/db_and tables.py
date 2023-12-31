import mysql.connector as connector

connection=connector.connect(user="root",password="Nerissa3091?")
cursor = connection.cursor()

create_query = """CREATE DATABASE little_lemon;"""
cursor.execute(create_query)

cursor.execute("show databases")
for database in cursor:
    print(database)

cursor.execute("use little_lemon;")
connection.database


create_menuitem_table = """CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

cursor.execute(create_menuitem_table)

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


create_menu_table = """CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

cursor.execute(create_menu_table)

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


create_booking_table = """CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

cursor.execute(create_booking_table)

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


create_orders_table = """CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""

cursor.execute(create_orders_table)

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)