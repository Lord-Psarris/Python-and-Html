import sqlite3 as sql

# connection
connection = sql.connect('TeeDb')

# the cursor
cursor = connection.cursor()

createDb = "CREATE TABLE 'customers' ('id' integer PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' VARCHAR(255) NOT NULL," \
           " 'email'  VARCHAR(255) NOT NULL, 'password' VARCHAR(255) NOT NULL, 'phone' char(11))"

# execute
cursor.execute(createDb)

# commit
connection.commit()
