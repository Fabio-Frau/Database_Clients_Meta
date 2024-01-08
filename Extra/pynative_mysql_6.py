import mysql.connector

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    print("Laptop table before deleting a row")
    sql_select_query = "SELECT * FROM Laptop WHERE Id = 7"
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    sql_delete_query = "DELETE FROM Laptop WHERE Id = 7"
    cursor.execute(sql_delete_query)
    connection.commit()
    print("Number of rows deleted", cursor.rowcount)

    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    if len(record) == 0:
        print("Record deleted successfully")

except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Use Python Variable in a SQL query to delete data from the table
print("Use Python Variable in a SQL query to delete data from the table")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    sql_delete_query = "DELETE FROM Laptop WHERE Id = %s"

    laptopId = 6
    cursor.execute(sql_delete_query, (laptopId,))
    connection.commit()
    print("Record deleted succesfully")

except mysql.connector.Error as error:
    print("Failed to Delete record from table: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Python Delete Multiple Rows from a MySQL Table
print("Python Delete Multiple Rows from a MySQL Table")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    sql_delete_query ="DELETE FROM Laptop WHERE Id = %s"
    records_to_delete = [(6,), (5,)]
    cursor.executemany(sql_delete_query, records_to_delete)
    connection.commit()
    print(cursor.rowcount, "Record deleted successfully")

except mysql.connector.Error as error:
    print("Failed to delete records from MySQL table: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Delete MySQL Table column from Python
print("Delete MySQL Table column from Python")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    alter_column = "ALTER TABLE Laptop DROP COLUMN Purchase_Date"
    cursor.execute(alter_column)
    connection.commit()
    print("Column deleted successfully")

except mysql.connector.Error as error:
    print("Failed to delete column: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Delete All rows from a table in Python
print("Delete All rows from a table in Python")


try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    delete_all_rows = "TRUNCATE TABLE Laptop"
    cursor.execute(delete_all_rows)
    connection.commit()
    print("All record deleted successfully")

except mysql.connector.Error as error:
    print("Failed to delete all records from database table: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

#Delete MySQL Table and Database from Python
print("Delete MySQL Table and Database from Python")


try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    delete_table_query = "DROP TABLE Laptop"
    cursor.execute(delete_table_query)

    delete_database_query = "DROP DATABASE Electronics"
    cursor.execute(delete_database_query)
    connection.commit()
    print("Table and Database deleted successfully")

except mysql.connector.Error as error:
    print("Failed to delete table and database : {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#

