import mysql.connector as connector

connection = connector.connect(user = "mario", password = "cuisine")

cursor = connection.cursor()

cursor.execute("USE little_lemon")

join_query = """
SELECT MenuItems.Name, MenuItems.Type, MenuItems.Price,
Menus.Cuisine FROM MenuItems INNER JOIN Menus ON
MenuItems.ItemID=Menus.ItemID
"""

cursor.execute(join_query)

results = cursor.fetchall()

print(cursor.column_names)
for result in results:
    print(result)