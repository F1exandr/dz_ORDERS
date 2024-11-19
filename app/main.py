import os

from flask import Flask, render_template, flash, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from database import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form3 = LoginForm()
    if form3.validate_on_submit():
        from models import User
        name = form3.username.data
        data = User(name=form3.username.data, password=form3.pasword.data, is_active=False)
        db.session.add(data)
        db.session.commit()
        flash('ПОЛЬЗОВАТЕЛЬ ' + name + ' ЗАРЕГИСТРИРОВАН')
        return redirect(url_for('index'))
    return render_template('login.html', form2=form3)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
