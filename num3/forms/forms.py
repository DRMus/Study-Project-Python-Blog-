from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField, EmailField
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    firstname = StringField('Имя', validators=[DataRequired()])
    lastname = StringField('Фамилия', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    file = FileField('Файл')
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class MapForm(FlaskForm):
    search = StringField('Город', validators=[DataRequired()])
    submit = SubmitField('Найти')


class EditUserForm(FlaskForm):
    firstname = StringField('Имя')
    lastname = StringField('Фамилия')
    position = StringField('Должность')
    age = IntegerField('Возраст')
    email = EmailField('Email')
    file = FileField('Файл')
    password = PasswordField('Пароль')
    submit = SubmitField('Редактировать')
