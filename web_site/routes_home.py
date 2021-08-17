from flask import render_template, url_for, flash, redirect, request
from web_site import app
from web_site.models import User
from flask_login import current_user

@app.route("/")
@app.route("/index")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('landing'))
    return render_template('index.html',title="Home")


@app.route("/landing")
def landing():
    return render_template('landing_page.html',title="Home",user=current_user)
