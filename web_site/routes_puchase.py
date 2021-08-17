from flask import render_template, url_for, flash, redirect, session
from web_site import app, db
from web_site.models import User, Order_Details, Orders, Products
from flask_login import login_required

@app.route("/purchase")
@login_required
def purchase():
    order_id_key = 'order_id'
    items_in_cart = []
    # remove the session variable for this order
    if order_id_key in session:
        order_id = session[order_id_key]
        items_in_cart = db.session.query(Order_Details, Products).join(Products, Products.id == Order_Details.product_id).filter(Order_Details.order_id == order_id)
        session.pop(order_id_key)
        return render_template('purchase.html', title='Order Complete',items_in_cart=items_in_cart)


    return render_template('purchase.html', title='Order Complete',items_in_cart=items_in_cart)

@app.route("/view_cart")
@login_required
def view_cart():
    order_id_key = 'order_id'
    totalString = ''
    items_in_cart = []

    # check for an existing order
    if order_id_key in session:
        # use the order id to get the number of items in the cart
        order_id = session[order_id_key]
        #items_in_cart = Order_Details.query.filter_by(order_id = order_id).join(Products, Products.id = Order_Details.product_id)

        items_in_cart = db.session.query(Order_Details, Products).join(Products, Products.id == Order_Details.product_id).filter(Order_Details.order_id == order_id)
        total = 0
        for item in items_in_cart:
            total += item.Products.price
        total *= 1.10
        totalString = "${:.2f}".format(total)
        if items_in_cart.count() == 0:
            items_in_cart = []

    else:
        print("order not found")

    
    return render_template('view_cart.html',title='My Cart', items_in_cart=items_in_cart, total = totalString)