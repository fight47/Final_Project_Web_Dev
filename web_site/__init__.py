from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vvmi2QT39O5lQy22'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# this import has to come after app because routes requires it
from web_site import routes_home
from web_site import routes_admin
from web_site import routes_authentication
from web_site import routes_browse_products
from web_site import routes_puchase
from web_site import routes_build_database
