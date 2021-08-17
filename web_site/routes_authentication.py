from flask import render_template, url_for, flash, redirect, request
from web_site import app, db, bcrypt
from web_site.forms_authentication import LoginForm
from web_site.forms_sign_up import RegistrationForm
from web_site.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        # hash the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # create a new user account
        user = User(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password, address=form.address.data, city=form.city.data, state=form.state.data, zip=form.zip.data, phone_no=form.phone_no.data, is_admin=form.is_admin.data)
        print(user)
        # add the new user to the database
        db.session.add(user)
        db.session.commit()
        # tell the user that the account was created
        flash(f'Account created for {form.username.data}!', 'success')
        # go to the landing page
        return redirect(url_for("login",user=form.username.data))

    # render the sign up page
    return render_template('sign_up.html', title='Sign Up', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # check for a user with this email
        user = User.query.filter_by(email=form.email.data).first()
        # check to see if the password matches
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # log the user in
            login_user(user, remember=form.remember.data)
            return redirect(url_for('landing')) 
        else:
            # the username or password was incorrect
            flash('Login failed.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    # log the user out
    logout_user()
    # send the user to the home page
    return redirect(url_for('home')) 
