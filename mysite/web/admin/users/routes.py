from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mysite import db, bcrypt
from mysite.web.admin.users.models import User, Post
from mysite.web.admin.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from mysite.web.admin.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass
    return render_template('register.html', title='Register', form=form)

@users.route("/login",methods=['GET','POST'])
def userLogin():
    return render_template('login.html',title='Login Page')

@users.route('/forget_password')
def forgetPassword():
    return render_template('forgot-password.html',title='Forgot Password')

