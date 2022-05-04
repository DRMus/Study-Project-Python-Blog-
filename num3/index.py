from flask import Flask, url_for, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TobbiGod'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class ConnectBtn(FlaskForm):
    submit = SubmitField()


# @app.route('/auth/', methods=['GET', 'POST'])
# def auth_main():
#     signup = ConnectBtn()
#     log = ConnectBtn()
#     if signup.validate_on_submit():
#         print("hell")
#     elif log.validate_on_submit():
#         return redirect('/login/')
#     return render_template('auth.html', title="Вход", log=log, signup=signup)


@app.route('/auth/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html', title='Вход', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
