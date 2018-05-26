from flask import render_template, redirect, url_for, flash, request
from ..models import User
from flask_login import login_user, login_required, logout_user, current_user
from .. import db
from .forms import RegistrationForm, LoginForm
from . import admin

@admin.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,hash_pass = form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message('Welcome to Watchlist', 'email/welcome_user', user.email, user=user)
        # send_email(subject="Registration", sender=os.environ.get('MAIL_USERNAME'),recepients=[user.email],text_body='Test Email',html_body=render_template('500.html'))

        return redirect(url_for('admin.login'))
    
    title = "Create New Account"

    return render_template('admin/register.html',registration_form = form, title = title)

@admin.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')

    title = "Admin Login | BeauCar "
    return render_template('admin/login.html', login_form = login_form,title=title)