import sqlite3 as sql

# connection
connection = sql.connect('TeeDb')

# the cursor
cursor = connection.cursor()

# execute

# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('back the f* up custom hoodie', 7000.00,"
#                " '../static/assets/products/hoodies/back d f up.jpg', 'hoodies', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('fashion durag', 2000.00,"
#                " '../static/assets/products/durags/fashion durags.jpg', 'durag', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('black lives matter custom tee', 3500.00,"
#                " '../static/assets/products/tees/black lives matter.jpg', 'tees', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('Dripping simpson custom tee', 3500.00,"
#                " '../static/assets/products/tees/colored drip simpson.jpg', 'tees', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('Almighty Morty quality tee', 3600.00,"
#                " '../static/assets/products/tees/crazy morty tees.jpg', 'tees', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('Quality 100% cotton joggers', 7000.00,"
#                " '../static/assets/products/joggers/plain white joggers.jpg', 'jog', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('Drip hoodie', 7000.00,"
#                " '../static/assets/products/hoodies/blue drip hood.jpg', 'hoodies', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('high quality durag', 2000.00,"
#                " '../static/assets/products/durags/high quality durag.jpg', 'durag', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('high quality custom hoodie', 7000.00,"
#                " '../static/assets/products/hoodies/colored lips.jpg', 'hoodies', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('high quality black hoodie', 7000.00,"
#                " '../static/assets/products/hoodies/hood1.jpg', 'hoodies', 'Lorem ipsum dolor sit amet,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")
#
# cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
#                " product_description) VALUES('high quality fashion durag', 2000.00,"
#                " '../static/assets/products/durags/high quality fashion durag.jpg', 'durag', 'Lorem ipsum dolor sit,"
#                " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#                " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('Custom marshmellow hoodie', 7000.00,"
               " '../static/assets/products/hoodies/marshmellow smile.jpg', 'hoodies', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('High quality custom sweatshirt', 5000.00,"
               " '../static/assets/products/sweatshirts/designed sweat.jpg', 'sweat', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('100% cotton custom tee', 3500.00,"
               " '../static/assets/products/tees/dripping simpson.jpg', 'tees', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('Give Thanks customized tees', 3500.00,"
               " '../static/assets/products/tees/every living thing.jpg', 'tees', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('High quality blue joggers', 7000.00,"
               " '../static/assets/products/joggers/plain blue jogger.jpg', 'jog', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('Gods words are complete...', 3500.00,"
               " '../static/assets/products/tees/gods words r complete.jpg', 'tees', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('Black quality custom tee', 3500.00,"
               " '../static/assets/products/tees/i am a boy.jpg', 'tees', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('high quality plain white hoodie', 7000.00,"
               " '../static/assets/products/hoodies/plain white hood.jpg', 'hoodies', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('I give zero f*s...', 3500.00,"
               " '../static/assets/products/tees/i give zero fs.jpg', 'tees', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

cursor.execute("INSERT INTO products (product_name, product_price, product_image, product_category,"
               " product_description) VALUES('High quality romantic tee', 3600.00,"
               " '../static/assets/products/tees/kiss tee 1.jpg', 'tees', 'Lorem ipsum dolor sit,"
               " consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
               " Ut enim ad minim veniam, quis nostrud exercitation ullamc');")

# ('back the f*ck up custom tee', 7000.00, 'assets/products/hoodies/back d f up.jpg', 'hoodies')

# commit
connection.commit()

# then u close the file/connection
connection.close()
