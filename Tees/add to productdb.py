import sqlite3 as sql


def product_add(name, price, image, category, description):
    # connection
    connection = sql.connect('TeeDb')

    # the cursor
    cursor = connection.cursor()

    s = f"INSERT INTO products (product_name, product_price, product_image, product_category, product_description)" \
        f" VALUES('{name}', {price}, '{image}', '{category}', '{description}');"
    cursor.execute(s)

    # commit
    connection.commit()

    # then u close the file/connection
    connection.close()
