from flask import render_template, url_for, flash, redirect
from web_site import app
from web_site import db

@app.route("/build_database")
def build_database():
    db.create_all()
    db.session.commit()
    return render_template('index.html',title='Home')

