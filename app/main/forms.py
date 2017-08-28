from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Email, Length


class FeedbackForm(FlaskForm):
    name = StringField('Ваше имя')
    email = StringField('Ваш email', validators=[DataRequired(), Length(1, 64), Email('Неверный email-адрес')])
    message = TextAreaField('Сообщение')
    submit = SubmitField('Отправить')
