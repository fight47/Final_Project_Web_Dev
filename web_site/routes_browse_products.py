from flask import render_template, url_for, flash, redirect, session, request, jsonify
from web_site import app, db
from web_site.models import User, Products, Orders, Order_Details
from flask_login import login_required, current_user
from datetime import date

@app.route("/browse_products")
@login_required
def browse_products():
    order_id = 0
    # products = Products.query.all()
    page = request.args.get('page', 1, type=int)
    products = Products.query.order_by(Products.id.asc()).paginate(page=page, per_page=2)
    items_in_cart_count = 0
    items_in_cart = []
    
    order_id_key = 'order_id'
    # check for an existing order
    if order_id_key in session:
        # use the order id to get the number of items in the cart
        order_id = session[order_id_key]
        items_in_cart = Order_Details.query.filter_by(order_id = order_id)
        items_in_cart_count = items_in_cart.count()
        if items_in_cart_count == 0:
            items_in_cart = []

    
    return render_template('browse_products.html',title='Shop', products=products, items_in_cart_count=items_in_cart_count)

@app.route("/add_to_cart", methods=['GET', 'POST'])
@login_required
def add_to_cart():
    print("entered add_to_cart")
    print('user id ' + str(current_user.id))
    product_id = request.form['product_id']
    print(product_id)
    order_id_key = 'order_id'
    order_id = 0
    
    # check for an existing order
    if order_id_key in session:
        order_id = session[order_id_key]
    else:
        # start a new order
        order = Orders(user_id = current_user.id, order_date=date.today())
        db.session.add(order)
        db.session.commit()
        # save the order to session memory
        session[order_id_key] = order.id 
        order_id = order.id

    order_detail = Order_Details(order_id = order_id, product_id = product_id)
    db.session.add(order_detail)
    db.session.commit()

    items_in_cart = Order_Details.query.filter_by(order_id = order_id)
    items_in_cart_count = items_in_cart.count()
    if items_in_cart_count == 0:
        items_in_cart = []
    # products = Products.query.all()
    page = request.args.get('page', 1, type=int)
    products = Products.query.order_by(Products.id.desc()).paginate(page=page, per_page=2)
    return jsonify({'result': 'success', 'items_in_cart_count' : items_in_cart_count})

@app.route("/delete_from_cart/<int:product_id>/update", methods=['GET', 'POST'])
@login_required
def delete_from_cart(product_id):
    print("entered delete_from_cart")
    print('product id ' + str(product_id))
    print('user id ' + str(current_user.id))

    order_id_key = 'order_id'
    
    order_id = session[order_id_key]
    try:
        order_detail = Order_Details.query.filter_by(order_id=order_id,product_id=product_id)[0]
        
        db.session.delete(order_detail)
        db.session.commit()
    except Exception:
        pass
    return redirect(url_for('view_cart'))
