import datetime
import os

from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from forms.forms import SignUpForm, LoginForm, MapForm
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
# noinspection PyUnresolvedReferences
from data.news import News
# noinspection PyUnresolvedReferences
from data.users import User
# noinspection PyUnresolvedReferences
from data import db_session
from num3.main import Maper

app = Flask(__name__)

UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['SECRET_KEY'] = 'TobbiGod'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(user_id, db_sess, User)


def create_user(firstname, lastname, position, age, email, password, filename='temp.jpg'):
    user = User(firstname=firstname, lastname=lastname, position=position,
                age=age, email=email, filename=filename)
    user.set_password(password)
    try:
        db_sess.add(user)
        db_sess.commit()
        print('OK')
    except RuntimeError:
        print(RuntimeError)


@app.route('/')
def auth_main():
    if current_user.is_authenticated:
        return redirect(url_for('users_page'))
    return render_template('auth.html', title="Вход")


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(request.args.get('next') or url_for('users_page'))
        return render_template('login.html', title='Вход', form=form, err=True)
    return render_template('login.html', title='Вход', form=form, err=False)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('users_page'))
    form = SignUpForm()
    if form.validate_on_submit():
        if form.file.data:
            time = datetime.datetime.now()
            upload_file(form.file.data, time)
            create_user(form.firstname.data, form.lastname.data, form.position.data, form.age.data, form.email.data,
                        form.password.data, secure_filename(str(time) + form.file.data.filename))
        else:
            create_user(form.firstname.data, form.lastname.data, form.position.data, form.age.data, form.email.data,
                        form.password.data)
        return redirect(url_for('login'))

    return render_template('signup.html', title='Регистрация', form=form)


@app.route('/users/', methods=['GET', 'POST'])
@login_required
def users_page():
    users = db_sess.query(User).all()
    return render_template('users.html', title='Пользователи', users=users)


@app.route('/map/', methods=['GET', 'POST'])
@login_required
def maper():
    form = MapForm()
    if form.validate_on_submit():
        is_find = Maper().create_map(form.search.data)
        if is_find:
            return redirect(request.url)
        else:
            return render_template('map.html', title='Карта', form=form, err=True)
    return render_template('map.html', title='Карта', form=form, err=False)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    print('выход из аккаунта')
    return redirect(url_for('auth_main'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', title="Страница не найдена"), 404


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(file, time):
    if file and allowed_file(file.filename):
        filename = secure_filename(str(time) + file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        print('No selected file')
        return redirect(request.url)


if __name__ == '__main__':
    db_session.global_init("db/site.db")
    db_sess = db_session.create_session()
    app.run(port=8080, host='127.0.0.1')
