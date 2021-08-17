from flask_login import UserMixin
from datetime import datetime
from web_site import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    city = db.Column(db.String(50), unique=False, nullable=False)
    state = db.Column(db.String(50), unique=False, nullable=False)
    zip = db.Column(db.String(10), unique=False, nullable=False)
    phone_no = db.Column(db.String(16), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.is_admin}')"


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    image_path = db.Column(db.String(500), unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"Products('{self.name}', '{self.price}')"


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    order_date = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f"Products('{self.id}', '{self.user_id}')"


class Order_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, unique=False, nullable=False)
    product_id = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"Products('{self.id}', '{self.order_id}', '{self.product_id}')"
