from flask_app.models import product, user
from flask_app import app, stripe, stripe_keys
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

# NOTE DISPLAYS/RENDERS


@app.route('/')
def home():

    return render_template("home.html")


@app.route("/team")
def team_page():

    return render_template("team.html")


@app.route("/cart")
def display_profile():

    if "uuid" not in session:
        return redirect("/")

    cart = user.Users.users_cart({"id": session["uuid"]})

    return render_template("cart.html",
                           user=user.Users.users_with_address({'id': session["uuid"]}),
                           cart=cart,
                           key=stripe_keys["publishable_key"])


@app.route("/charge")
def charge_page():
    if "purchase" not in session:
        return redirect("/")

    customer = user.Users.user_by_id({"id": session["uuid"]})
    return render_template("charge.html", customer=customer, total=int(session["purchase"]))
# NOTE ACTIONS/POSTS


@app.route('/charge/verify', methods=['POST'])
def charge():

    customer = user.Users.user_by_id({'id': session["uuid"]})
    cart = user.Users.users_cart({"id": session["uuid"]})
    total = 0
    for item in cart.cart:
        total += item.price
        product.Products.remove_from_cart({"product_id": item.id})

    customer = stripe.Customer.create(
        email=customer.email,
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=total*100,
        currency='usd',
        description="Placed An Order"
    )

    session['purchase'] = total

    return redirect('/charge')


@ app.route('/verify/register', methods=["POST"])
def verify_register():

    if not user.Users.validate_register(request.form):
        return redirect('/merch')

    hashed_pw = bcrypt.generate_password_hash(request.form["password"])

    user_data = {
        **request.form,
        "password": hashed_pw,
        "email": request.form["email"].lower(),
        "full_name": f"{request.form['first_name']} {request.form['last_name']}"
    }

    session["uuid"] = user.Users.insert_user(user_data)
    return redirect("/merch")


@ app.route("/verify/login", methods=["POST"])
def verify_login():
    user_check = user.Users.user_by_email({"email": request.form["email"]})

    if not user.Users.validate_login(user_check, {"input_pw": request.form["password"]}):
        return redirect("/merch")

    session["uuid"] = user_check.id

    if user_check.id == 1:
        session['admin'] = True

    flash("Logged In Successfully", "logged-in")
    return redirect("/merch")


@ app.route('/logout')
def logout():
    session.clear()
    return redirect("/")
