import sqlite3 as sql

# connection
connection = sql.connect('TeeDb')

# the cursor
cursor = connection.cursor()

createDb = "CREATE TABLE 'orders' ('id' integer PRIMARY KEY AUTOINCREMENT NOT NULL," \
           " 'user' integer NOT NULL, 'product' integer NOT NULL, 'quantity' integer DEFAULT 1 NOT NULL," \
           " 'color' VARCHAR(10) NOT NULL, 'size' VARCHAR(3) NOT NULL," \
           "  'status' char(1) DEFAULT 0 NOT NULL);"

# execute
cursor.execute(createDb)

# commit
connection.commit()
