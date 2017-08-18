from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, DataRequired


class FeedbackForm(FlaskForm):
    name = StringField('Ваше имя')
    email = StringField('Ваш email', validators=[DataRequired('Это поле должно быть заполнено.')])
    message = TextAreaField('Сообщение')
    submit = SubmitField('Отправить')
