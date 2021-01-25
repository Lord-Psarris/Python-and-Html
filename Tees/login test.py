import sqlite3 as sql

# connection
connection = sql.connect('TeeDb')

# the cursor
cursor = connection.cursor()

# to fetch the data
co = "SELECT * FROM orders where status=1;"

# DROP TABLE customers

cursor.execute(co)

ans = cursor.fetchall()

print(ans)

# then u close the file/connection
connection.close()