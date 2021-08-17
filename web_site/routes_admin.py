from flask import render_template, url_for, flash, redirect, request
from web_site import app, db
from web_site.forms_admin import AdminEditProductsForm
from web_site.models import Products
import os
import secrets
from PIL import Image
from flask_login import login_required

def save_image(uploaded_image):
    # get a random string for file name to keep from having filename conflicts
    image_file_name = secrets.token_hex(12)
    # get file extension
    _ , file_extension = os.path.splitext(uploaded_image.filename)
    # assemble the file name
    filename = image_file_name + file_extension
    # get the full path
    image_path = os.path.join(app.root_path, 'static/images', filename)
    # save the image
    # uploaded_image.save(image_path)
    # resize the image to a standard size
    output_size = (2048, 2048)
    image = Image.open(uploaded_image)
    image.thumbnail(output_size)
    # save the resized image
    image.save(image_path)

    return filename
def delete_image(image_path):
    print(image_path)
    os.remove(image_path)


@app.route("/admin_add_inventory", methods=['GET', 'POST'])
@login_required
def admin_add_inventory():
    form = AdminEditProductsForm()
    form.submit.label.text = 'Add Item'
    if form.validate_on_submit():
        print(form)
        if form.upload_image.data:
            image_path = save_image(form.upload_image.data)
        product = Products(name=form.name.data, description=form.description.data, price=form.price.data, image_path=image_path)
        db.session.add(product)
        db.session.commit()
        flash(f'Product added {form.name.data}!', 'success')
        return redirect(url_for('admin_view_inventory'))
    return render_template('add_inventory.html',title="Add Inventory", form=form)

@app.route("/admin_update_inventory/<int:product_id>/update", methods=['GET', 'POST'])
@login_required
def admin_update_inventory(product_id):
    product = Products.query.get_or_404(product_id)
    form = AdminEditProductsForm()
    form.submit.label.text = 'Update Item'
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        if form.upload_image.data:
            image_path = os.path.join(app.root_path, 'static/images', product.image_path)
            delete_image(image_path)
            image_path = save_image(form.upload_image.data)
            product.image_path = image_path
        db.session.commit()
        flash('Your product has been updated!', 'success')
        return redirect(url_for('admin_view_inventory'))
    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price
    return render_template('add_inventory.html', title='Update Product',
                           form=form, legend='Update Product', update=1)

@app.route("/admin_delete_inventory/<int:product_id>/update", methods=['GET', 'POST'])
@login_required
def admin_delete_inventory(product_id):
    product = Products.query.filter_by(id=product_id).first()
 
    image_path = os.path.join(app.root_path, 'static/images', product.image_path)
    delete_image(image_path)

    db.session.delete(product)
    db.session.commit()

    flash('The item was sucsessfully deleted from the database.', 'success')
    return redirect(url_for('admin_view_inventory'))

@app.route("/admin_view_inventory")
@login_required
def admin_view_inventory():
    page = request.args.get('page', 1, type=int)
    products = Products.query.order_by(Products.id.asc()).paginate(page=page, per_page=3)
    print(products)
    return render_template('view_inventory.html', title='View Inventory', products=products)