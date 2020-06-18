from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mysite import db, bcrypt

admin = Blueprint('admin_home', __name__)


@admin.route("/home", methods=['GET', 'POST'])
def adminHome():
    return render_template('adminHome.html', title='Register')

