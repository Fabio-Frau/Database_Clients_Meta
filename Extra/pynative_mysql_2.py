import mysql.connector

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    mysql_create_table_query = """CREATE TABLE Laptop (
                            Id int(11) NOT NULL,
                            Name varchar(250) NOT NULL,
                            Price float NOT NULL,
                            Purchase_date Date NOT NULL,
                            PRIMARY KEY(Id))"""
    
    cursor = connection.cursor()
    result = cursor.execute(mysql_create_table_query)
    print("Laptop Table created succesfully")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")