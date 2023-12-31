import mysql.connector as connector
from mysql.connector import errorcode

try:
    connection = connector.connect(user = "root", password = "Nerissa3091?", 
                                host = "localhost", database = "magazzino",
                                port  = 3306)

    print(connection.get_server_info())

# except connector.Error as err:
#     print(err.errno)

except connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Connection user or password are incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database does not exists")
    else:
        print(err)



