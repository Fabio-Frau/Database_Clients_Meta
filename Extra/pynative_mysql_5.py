import mysql.connector
from datetime import datetime

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()

    print("Before updating a record")
    sql_select_query = """SELECT * FROM Laptop WHERE Id = 2"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    sql_update_query = """UPDATE Laptop SET Price = 7000 WHERE Id = 2"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully")

    print("Afer updating record")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Use a Python variable in MySQL Update query
print("Use a Python variable in MySQL Update query")

def update_laptop_price(id, price):
    try:
        connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                            user = "mario", password ="cuisine")
        
        cursor = connection.cursor()
        sql_update_query = "UPDATE Laptop SET Price = %s WHERE Id = %s"
        input_data = (price, id)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print("Record Updated successfully")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


update_laptop_price(7500, 2)
update_laptop_price(9000, 3)


#Update Multiple Rows of MySQL Table using Python
print("Update Multiple Rows of MySQL Table using Python")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    sql_update_query = "UPDATE Laptop SET Price = %s WHERE Id = %s"
    records_to_update = [(3000,3), (2750,4)]
    cursor.executemany(sql_update_query, records_to_update)
    connection.commit()

    print(cursor.rowcount, "Record of Laptop table updated successfully")

except mysql.connector.Error as error:
    print("Failed to update records to database: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Python update multiple Columns of MySQL table
print("Python update multiple Columns of MySQL table")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    sql_update_query = "UPDATE Laptop SET Name = %s, Price = %s WHERE Id = %s"

    name = "HP Pavilion"
    price = 2200
    id = 4
    input = (name, price, id)

    cursor.execute(sql_update_query, input)
    connection.commit()
    print("multiple columns updated succesfully")

except mysql.connector.Error as error:
    print("Failed to update columns of table: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Update Datetime and timestamp column of a MySQL table from Python
print("Update Datetime and timestamp column of a MySQL table from Python")


try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    sql_update_query = "UPDATE Laptop SET Purchase_date = %s WHERE Id = %s"

    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    id = 2
    input = (formatted_date, id)
    cursor.execute(sql_update_query, input)
    connection.commit()
    print("Purchased Date updated succesfully")

except mysql.connector.Error as error:
    print("Failed to update purchase date {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")




