from flask_app.models import product, user
from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route("/merch")
def merch_page():

    if "filter" in session:
        return render_template("merch.html", products=product.Products.get_by_category({"id": session["filter"]}))

    return render_template("merch.html", products=product.Products.get_all_products())


@app.route("/cart/add/<int:product_id>")
def add_cart(product_id):

    if"uuid" not in session:
        return redirect("/")

    data = {"user_id": session["uuid"],
            "product_id": product_id}
    product.Products.add_to_cart(data)
    return redirect("/merch")


@app.route("/cart/remove/<int:product_id>")
def remove_cart(product_id):

    if"uuid" not in session:
        return redirect("/")

    data = {"product_id": product_id}
    product.Products.remove_from_cart(data)
    return redirect("/cart")


@app.route("/merch/filter", methods=["POST"])
def filter_merch():

    if request.form['filter'] == "4" and "filter" in session:
        session.pop("filter")
        return redirect("/merch")

    session["filter"] = request.form['filter']
    return redirect("/merch")
