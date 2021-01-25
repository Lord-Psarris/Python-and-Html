import sqlite3 as sql

# connection
connection = sql.connect('TeeDb')

# the cursor
cursor = connection.cursor()

createDb = "CREATE TABLE 'products' ('id' integer PRIMARY KEY AUTOINCREMENT NOT NULL, 'product_name' VARCHAR(255)" \
           " NOT NULL, 'product_price' integer NOT NULL, 'product_image'  VARCHAR(255) NOT NULL, 'product_category'" \
           "  VARCHAR(255) NOT NULL, 'product_description'  VARCHAR(1024) NOT NULL);"

# execute
cursor.execute(createDb)

# commit
connection.commit()

# then u close the file/connection
connection.close()
