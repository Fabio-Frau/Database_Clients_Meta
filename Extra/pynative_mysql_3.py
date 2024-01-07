#execute INSERT Query from Python to add a new row
import mysql.connector
from datetime import datetime

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    insert_stmt = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                    VALUES (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14');"""
    
    cursor = connection.cursor()
    cursor.execute(insert_stmt)
    connection.commit()
    print(cursor.rowcount, "Record inserted succesfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection in closed")


# Use Python Variables in a MySQL Insert Query
        
def insert_variable_into_table(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
        
        cursor = connection.cursor()
        mysql_insert_stmt = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                            VALUES (%s, %s, %s, %s)"""
        
        record = (id, name, price, purchase_date)
        cursor.execute(mysql_insert_stmt, record)
        connection.commit()
        print("Record inserted succesfully into Laptop table")
    
    except:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySql connection is closed")

insert_variable_into_table(2, "Area 51M", 6999, '2019-04-14')
insert_variable_into_table(3, "MacBook Pro", 2499, '2019-06-20')

#Insert multiple rows into MySQL table using the cursor’s executemany()

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
        
    mysql_insert_stmt = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                         VALUES (%s, %s, %s, %s)"""
        
    records_to_insert = [(4, "HP Pavillon Power", 1999, '2019-01-11'),
                        (5, "MSI WS75 9TL-496", 5799, '2019-02-27'),
                        (6, "Microsoft Surface", 2330, '2019-07-23')]
        
    cursor = connection.cursor()
    cursor.executemany(mysql_insert_stmt, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted succesfully into Laptop table")
        

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        

# Insert timestamp and DateTime into a MySQL table using Python

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    mysql_insert_stmt = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                            VALUES(%s, %s, %s, %s)"""
    
    cursor = connection.cursor()
    current_Date = datetime.now()

    formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
    insert_tuple = (7, "Acer Predator Triton", 2435, current_Date)

    result = cursor.execute(mysql_insert_stmt, insert_tuple)
    connection.commit()
    print("Date Record inserted successfully")

except mysql.connector.Error as error:
    connection.rollback()
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")