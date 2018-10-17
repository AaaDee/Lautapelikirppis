from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm


@app.route('/auth/login', methods = ['GET', 'POST'])
def auth_login():
    if request.method == 'GET':
        return render_template('auth/loginform.html', form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template('auth/loginform.html', form = form,
                               error = 'Käyttäjänimeä ei löytynyt tai salasana on väärin')


    login_user(user)
    return redirect(url_for('index')) 

@app.route('/auth/logout')
def auth_logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/auth/register', methods = ['GET', 'POST'])
def auth_register():
    if request.method == 'GET':
        return render_template('auth/registerform.html', form = RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate():
            return render_template('auth/registerform.html', form = form)
    
    username = form.username.data
    password = form.password.data
    email = form.email.data
    location = form.location.data

    user = User(username, password, email, location)
    db.session().add(user)
    db.session().commit()

    return redirect(url_for('auth_login'))

@app.route('/mypage', methods = ['GET'])
@login_required
def auth_mypage():
    return render_template('auth/mypage.html', user = current_user)