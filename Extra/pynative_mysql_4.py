import mysql.connector

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")

    sql_select_query = "SELECT * FROM Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_query)

    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Use Python variables as parameters in MySQL Select Query
print("Use Python variables as parameters in MySQL Select Query")
        
def get_laptop_detail(id):
    try:
        connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
        
        cursor = connection.cursor()
        sql_select_query = """SELECT * FROM Laptop WHERE id = %s"""
        
        cursor.execute(sql_select_query, (id,))

        record = cursor.fetchall()

        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Salary  = ", row[3], "\n")

    except mysql.connector.Error as e:
        print("Failed to get record from MySQL table: {}".format(e))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


get_laptop_detail(1)
get_laptop_detail(2)


#Select limited rows from MySQL table using fetchmany and fetchone
print("Select limited rows from MySQL table using fetchmany and fetchone")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                    user = "mario", password ="cuisine")
    
    sql_select_query = "SELECT * FROM Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    row_count = 2
    records = cursor.fetchmany(row_count)

    print("Total number of rows is: ", cursor.rowcount)
    print("Printing ", row_count, " Laptop record using cursor.fetchmany()")

    for row in records:
        print(row)

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection is closed")


#Fetch single row from MySQL table using cursor’s fetchone
print("Fetch single row from MySQL table using cursor’s fetchone")
        
try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                    user = "mario", password ="cuisine")

    sql_select_query = "SELECT * FROM Laptop"
    cursor = connection.cursor(buffered=True)
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Python Fetch MySQL row using the column names
print("Python Fetch MySQL row using the column names")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                    user = "mario", password ="cuisine")

    sql_select_query = "SELECT * FROM Laptop"

    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    print("Fetching each row using column name")
    for row in records:
        id = row["Id"]
        name = row["Name"]
        price = row["Price"]
        purchase_date = row["Purchase_date"]
        print(id, name, price, purchase_date)

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Select MySQL column value into a Python Variable
print("Select MySQL column value into a Python Variable")


try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                    user = "mario", password ="cuisine")
    
    sql_query = "SELECT price FROM Laptop WHERE Id = %s"
    id = (2,)
    cursor = connection.cursor()
    cursor.execute(sql_query, id)
    record = cursor.fetchone()

    price = float(record[0])
    print("Laptop price is : ", price)

except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


