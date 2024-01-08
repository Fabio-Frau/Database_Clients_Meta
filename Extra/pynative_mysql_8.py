import mysql.connector 

#Example to insert data into MySQL table using Parameterized Query
print("Example to insert data into MySQL table using Parameterized Query")
try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor(prepared=True)
    sql_insert_query = "INSERT INTO Employee (id, Name, Joining_date, salary) \
                        VALUES (%s, %s, %s , %s)"
    
    tuple1 = (1, "Json", "2019-03-23", 9000)
    tuple2 = (2, "Emma", "2019-05-19", 9500)

    cursor.execute(sql_insert_query, tuple1)
    cursor.execute(sql_insert_query, tuple2)
    connection.commit()
    print("Data inserted successfully into employee table using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#Use Parameterized Query Update data of MySQL table
print("Use Parameterized Query Update data of MySQL table")

try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor.(prepared= )