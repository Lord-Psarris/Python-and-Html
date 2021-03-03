from flask import Flask, render_template, request, session, redirect, url_for, escape
import sqlite3 as sql

# to do
"""
make the products go to more than one page
add search feature
resize photos
cryptography
check how red looks
"""

app = Flask(__name__)
app.secret_key = 'The_talking_tees'


@app.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        connection = sql.connect('TeeDb')
        # the cursor
        cursor = connection.cursor()
        names = str(request.form.get("username"))
        email = str(request.form.get("email"))
        phone = str(request.form.get("phone"))
        password = str(request.form.get("password"))
        password_confirm = str(request.form.get("password_two"))
        cursor.execute("SELECT name, password FROM customers WHERE name=? OR email=?",
                       (names, email))
        res = cursor.fetchone()
        if password == password_confirm:
            if res:
                return "you have already signed up"
            else:
                s = f"INSERT INTO customers (name, email, password, phone) VALUES('{names}', '{email}', '{password}'," \
                    f" '{phone}');"
                cursor.execute(s)
                connection.commit()
                return "redirect"
        else:
            return "passwords aren't the same"
    return render_template("sign-up.html")


@app.route("/login", methods=["GET"])
def sign_in():
    return render_template("sign-in.html")


@app.route("/log", methods=["POST"])
def sign():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    names = str(request.form.get("username"))
    password = str(request.form.get("password"))

    cursor.execute("SELECT id FROM customers WHERE name=? OR email=?",
                   (names, names))
    res = cursor.fetchone()
    if res:
        pass_id = str(res[0])
        cursor.execute("SELECT password FROM customers WHERE id=?", pass_id)
        rep = cursor.fetchone()
        pass_word = rep[0]
        if password == pass_word:
            session['user_key'] = pass_id
            name = session['user_key']
            name = str(name)
            if name:
                cursor.execute("SELECT name FROM customers WHERE id=?", name)
                names = cursor.fetchall()
                for name in names:
                    name = name[0]
                    if len(name) > 7:
                        ram = name
                        sub = ram[7:]
                        sub = str(sub)
                        name = name.replace(sub, "...")
                        session["user_name"] = name
                        session["yum"] = True
                    elif len(name) <= 7:
                        session["user_name"] = name
                        session["yum"] = True
                    user_id = session["user_key"]
                    cursor.execute("SELECT COUNT(*) FROM orders WHERE user=?", user_id)
                    no = cursor.fetchone()
                    session["cart_no"] = no[0]
                    # session["cart_items"] = ""
            else:
                session["yum"] = False
                pass
        elif password != pass_word:
            return "password incorrect"
    else:
        return "username or email doesn\'t exist"
    # end of sql
    connection.commit()
    # create a mail
    return "redirect"


@app.route("/reset", methods=["POST", "GET"])
def reset():
    if request.method == "POST":
        connection = sql.connect('TeeDb')
        cursor = connection.cursor()
        names = str(request.form.get("username"))
        email = str(request.form.get("email"))
        password = str(request.form.get("password"))
        password_2 = str(request.form.get("password_confirm"))

        cursor.execute("SELECT name, password FROM customers WHERE name=? AND email=?", (names, email))
        res = cursor.fetchone()
        if res:
            if password == password_2:
                cursor.execute("UPDATE customers SET password=? where email=? AND name=?", (password_2, email, names))
                connection.commit()
                return "redirect"
                # suppose to redirect them to a confirmation page
            else:
                return "passwords aren\'t the same"
        else:
            return "username or email does not exist"
    return render_template("reset.html")


@app.route("/")
def index():
    try:
        if session["cart_no"]:
            return render_template("index.html", name=session["user_name"], yum=session["yum"], cart=session["cart_no"])
        else:
            cart = 0
            return render_template("index.html", name=session["user_name"], yum=session["yum"], cart=cart)
    except KeyError:
        yum = False
        cart = 0
        return render_template("index.html", yum=yum, cart=cart)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/shop")
def shop():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()

    # for product collecting
    collect = "SELECT * FROM products;"
    cursor.execute(collect)
    products = cursor.fetchall()

    try:
        return render_template("shop.html", name=session["user_name"], yum=session["yum"], products=products,
                               cart=session["cart_no"])
    except KeyError:
        yum = False
        cart_ = 0
        return render_template("shop.html", yum=yum, products=products, cart=cart_)


@app.route("/details", methods=["POST"])
def details():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    id_ = int(request.form.get("detail"))
    cursor.execute(f"SELECT * FROM products WHERE id={id_}")
    products = cursor.fetchall()
    return str(products)


@app.route("/addtocart", methods=["POST"])
def add_to_cart():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    id_ = int(request.form.get("cartId"))
    try:
        if session["user_key"]:
            product_id = str(id_)
            user_id = str(session["user_key"])
            cursor.execute("SELECT id FROM orders WHERE user=? AND product=?",
                           (user_id, product_id))
            # "SELECT COUNT(*) FROM orders WHERE user=3;"
            res = cursor.fetchone()
            if res:
                return "product is in your cart"
            else:
                s = f"INSERT INTO orders (user,product,color,size) VALUES({user_id}, {product_id}, '', '');"
                cursor.execute(s)
                res = cursor.fetchone()
                connection.commit()
                user_id = session["user_key"]
                cursor.execute("SELECT COUNT(*) FROM orders WHERE user=?", user_id)
                no = cursor.fetchone()
                session["cart_no"] = no[0]
                return "product has been added to cart"
    except KeyError:
        return "you are not logged in"


@app.route("/cart")
def cart():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    session["cart_items"] = []
    price = []
    try:
        if session["user_key"]:
            user = session["user_key"]
            cursor.execute("SELECT product FROM orders WHERE user=?", user)
            reps = cursor.fetchall()
            rip = ""
            quantity = ""
            pin = 0
            number = 0
            complete_order = False
            if reps:
                for rep in reps:
                    for rip in rep:
                        rip = str(rip)
                        cursor.execute(f"SELECT * FROM products WHERE id={rip}")
                        inna = cursor.fetchone()
                        cursor.execute("SELECT quantity FROM orders WHERE user=? AND product=?", (user, rip))
                        ibba = cursor.fetchone()
                        quantity = ibba[0]
                        inna = list(inna)
                        inna.append(quantity)
                        cursor.execute("SELECT size, color FROM orders WHERE user=? AND product=?", (user, rip))
                        idda = cursor.fetchone()
                        if idda:
                            size = idda[0]
                            color = idda[1]
                            inna.append(size)
                            inna.append(color)
                        inna = tuple(inna)
                        session["cart_items"].append(inna)
                        cursor.execute(f"SELECT product_price FROM products WHERE id={rip}")
                        prior = cursor.fetchall()
                        prior = prior * quantity
                        price.append(prior)
                        number = number + quantity
                cart_true = True
            else:
                cart_true = False
            items = session["cart_items"]
            for p in price:
                for i in p:
                    pin = pin + i[0]
            subtotal = pin
            session["subtotal"] = subtotal
            total = pin + 2000
            session["total"] = total
            cursor.execute(f"SELECT size, color FROM orders WHERE user={user}")
            forl = cursor.fetchall()
            col_list = []
            for fl in forl:
                for l in fl:
                    col_list.append(l)
            if "" in col_list:
                complete_order = False
            else:
                complete_order = True
            return render_template("cart.html", name=session["user_name"],
                                   yum=session["yum"], cart=session["cart_no"], items=items,
                                   number=number, subtotal=subtotal, total=total,
                                   carts=cart_true, co=complete_order)
    except KeyError:
        cart_true = False
        cart_ = 0
        yum = False
        return render_template("cart.html", yum=yum, cart=cart_, carts=cart_true)


@app.route("/remove", methods=["POST"])
def remove():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    p_id = str(request.form.get("pid"))
    user_id = session["user_key"]
    cursor.execute("DELETE FROM orders WHERE user=? AND product=?",
                   (user_id, p_id))
    connection.commit()
    cursor.execute("SELECT COUNT(*) FROM orders WHERE user=?", user_id)
    no = cursor.fetchone()
    session["cart_no"] = no[0]
    cursor.execute("SELECT id FROM orders WHERE user=?", user_id)
    no = cursor.fetchone()
    return "done"


@app.route("/clear", methods=["POST"])
def clear():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    p_id = str(request.form.get("claire"))
    user_id = session["user_key"]
    cursor.execute("DELETE FROM orders WHERE user=?", user_id)
    connection.commit()
    cursor.execute("SELECT COUNT(*) FROM orders WHERE user=?", user_id)
    no = cursor.fetchone()
    session["cart_no"] = no[0]
    cursor.execute("SELECT id FROM orders WHERE user=?", user_id)
    no = cursor.fetchone()
    return "done"


@app.route("/addquantity", methods=["POST"])
def quantity_plus():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    opp = str(request.form.get("plus"))
    user = session["user_key"]
    cursor.execute("SELECT quantity FROM orders WHERE user=? AND product=?", (user, opp))
    numb = cursor.fetchone()
    numb = numb[0]
    quantity_ = numb + 1
    cursor.execute("UPDATE orders SET quantity=? WHERE user=? AND product=?", (quantity_, user, opp))
    connection.commit()
    return "done"


@app.route("/subquantity", methods=["POST"])
def quantity_minus():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    opp = str(request.form.get("minus"))
    user = session["user_key"]
    cursor.execute("SELECT quantity FROM orders WHERE user=? AND product=?", (user, opp))
    numb = cursor.fetchone()
    numb = numb[0]
    quantity_ = 1
    if numb > 1:
        quantity_ = numb - 1
    cursor.execute("UPDATE orders SET quantity=? WHERE user=? AND product=?", (quantity_, user, opp))
    connection.commit()
    return "done"


@app.route("/size", methods=["POST"])
def sizes():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    size = str(request.form.get("size"))
    size_id = str(request.form.get("prod"))
    user = session["user_key"]
    cursor.execute("UPDATE orders SET size=? WHERE user=? AND product=?", (size, user, size_id))
    connection.commit()
    return size


@app.route("/color", methods=["POST"])
def colors():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    color = str(request.form.get("color"))
    color_id = str(request.form.get("prod"))
    user = session["user_key"]
    cursor.execute("UPDATE orders SET color=? WHERE user=? AND product=?", (color, user, color_id))
    connection.commit()
    return color


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        contact_name = str(request.form.get("contact_fname"))
        contact_last_name = str(request.form.get("contact_lname"))
        contact_email = str(request.form.get("contact_mail"))
        contact_comment = str(request.form.get("comment"))
        # do stuff with comment;
        # e.g mail the commenter some stuff;
        # mail the actual comment to yourself
    try:
        return render_template("contact.html", name=session["user_name"],
                               yum=session["yum"], cart=session["cart_no"])
    except KeyError:
        yum = False
        cart_ = 0
        return render_template("contact.html", yum=yum, cart=cart_)


@app.route("/about")
def about():
    try:
        return render_template("about.html", name=session["user_name"], yum=session["yum"], cart=session["cart_no"])
    except KeyError:
        yum = False
        cart_ = 0
        return render_template("about.html", yum=yum, cart=cart_)


@app.route("/checkout")
def checkout():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()

    user = session["user_key"]

    # for product collecting
    collect = f"SELECT * FROM products JOIN orders ON products.id" \
              f" = orders.product WHERE orders.user={user};"
    cursor.execute(collect)
    # SELECT * FROM products JOIN orders ON products.id = orders.product WHERE orders.user={user}
    orders = cursor.fetchall()
    cursor.execute(f"SELECT name, email, phone FROM customers WHERE id={user}")
    values = cursor.fetchall()
    name = values[0][0]
    mail = values[0][1]
    number = values[0][2]
    try:
        total = session["total"]
        subtotal = session["subtotal"]

        return render_template("checkout.html", name=session["user_name"]
                               , yum=session["yum"], cart=session["cart_no"],
                               products=orders, total=total, subtotal=subtotal,
                               first=name, mail=mail, number=number)
    except KeyError:
        yum = False
        cart_ = 0
        return render_template("checkout.html", yum=yum, cart=cart_)


@app.route("/checkout/order", methods=["POST"])
def order():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    user = session['user_key']
    first = str(request.form.get("firstName"))
    last = str(request.form.get("lastName"))
    address = str(request.form.get("address"))
    state = str(request.form.get("state"))
    town = str(request.form.get("town"))
    number = str(request.form.get("number"))
    email = str(request.form.get("email"))
    note = str(request.form.get("orderNote"))
    print(f"{first} {last} {address} {state} {town} {number} {email} {note}")
    cursor.execute(f"UPDATE orders SET status=1 where user={user};")
    connection.commit()
    return redirect(url_for('complete'))


@app.route("/customize/merch/uploads")
def custom():
    try:
        if session["cart_no"]:
            return render_template("custom.html", name=session["user_name"], yum=session["yum"],
                                   cart=session["cart_no"])
        else:
            cart = 0
            return render_template("custom.html", name=session["user_name"], yum=session["yum"], cart=cart)
    except KeyError:
        yum = False
        cart = 0
        return render_template("custom.html", yum=yum, cart=cart)


@app.route("/upload", methods=["POST"])
def upload():
    connection = sql.connect('TeeDb')
    cursor = connection.cursor()
    user = session['user_key']
    first = str(request.form.get("firstName"))
    last = str(request.form.get("lastName"))
    address = str(request.form.get("address"))
    state = str(request.form.get("state"))
    color = str(request.form.get("color"))
    size = str(request.form.get("size"))
    cloth = str(request.form.get("cloth"))
    number = str(request.form.get("number"))
    email = str(request.form.get("email"))
    print(f"{first} {last} {address} {state} {number} {email} {color} "
          f"{size} {cloth}")
    return redirect(url_for('complete'))


@app.route("/order")
def complete():
    carts = 0
    return render_template("order.html", name=session["user_name"], yum=session["yum"], cart=carts)


# needs to be done
@app.route("/privacy policy")
def privacy():
    return render_template("privacy.html")


@app.route("/shopping policy")
def shopping():
    return render_template("shopping.html")


@app.route("/return policy")
def returns():
    return render_template("returns.html")


@app.route("/terms and conditions")
def terms():
    return render_template("terms.html")


# needs to be done


# connection.close()

if __name__ == "__main__":
    app.run(debug=True)
