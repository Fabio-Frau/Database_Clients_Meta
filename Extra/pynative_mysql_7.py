import mysql.connector 

# #create the stored procedure
try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    create_procedure = "CREATE PROCEDURE get_laptop(IN d_Id INT)\
                        BEGIN\
                        SELECT * FROM Laptop WHERE Id = d_Id;\
                        END"
    
    print(create_procedure)

    cursor.execute(create_procedure)

except mysql.connector.Error as error:
    print("Failed to crate stored procedure: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



#calling the stored procedure
try:
    connection = mysql.connector.connect(host = "localhost", database ="Electronics",
                                        user = "mario", password ="cuisine")
    
    cursor = connection.cursor()
    cursor.callproc('get_laptop', [1,])
    print("Printing laptop details")
    for result in cursor.stored_results():
        print(result.fetchall())

except mysql.connector.Error as error:
    print("Failed to execute the stored procedure: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")