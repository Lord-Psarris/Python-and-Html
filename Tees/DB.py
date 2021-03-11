import sqlite3 as sql


def make_tables():
    # connection
    connection = sql.connect('TeeDb')

    # the cursor
    cursor = connection.cursor()

    customer_db = "CREATE TABLE IF NOT EXISTS 'customers' ('id' integer PRIMARY KEY AUTOINCREMENT NOT NULL," \
                  "'name' VARCHAR(255) NOT NULL, 'email'  VARCHAR(255) NOT NULL, 'password' VARCHAR(255) NOT NULL," \
                  "'phone' char(11))"

    order_db = "CREATE TABLE IF NOT EXISTS 'orders' ('id' integer PRIMARY KEY AUTOINCREMENT NOT NULL," \
               " 'user' integer NOT NULL, 'product' integer NOT NULL, 'quantity' integer DEFAULT 1 NOT NULL," \
               " 'color' VARCHAR(10) NOT NULL, 'size' VARCHAR(3) NOT NULL," \
               "  'status' char(1) DEFAULT 0 NOT NULL);"

    product_db = "CREATE TABLE IF NOT EXISTS 'products' ('id' integer PRIMARY KEY AUTOINCREMENT NOT NULL," \
                 "'product_name' VARCHAR(255) NOT NULL, 'product_price' integer NOT NULL," \
                 "'product_image'  VARCHAR(255) NOT NULL, 'product_category' VARCHAR(255) NOT NULL," \
                 "'product_description' VARCHAR(1024) NOT NULL);"

    # execute
    cursor.execute(customer_db)
    cursor.execute(order_db)
    cursor.execute(product_db)

    # commit
    connection.commit()


def test_log(main, where, what=None, value=None, others=None):
    connection = sql.connect('TeeDb')

    # the cursor
    cursor = connection.cursor()

    # to fetch the data
    if what is not None:
        co = f"SELECT {main} FROM {where} where {what}={value};"
    else:
        co = f"SELECT {main} FROM {where};"

    # DROP TABLE customers

    cursor.execute(co)

    ans = cursor.fetchall()

    return ans
