from flask import current_app, render_template
from flask_mail import Message
import flask_mail
from . import mail


__MESSAGE_SUBJECT = '[Omniliner] Сообщение из формы обратной связи'

flask_mail.message_policy = None


def send_email(template, **kwargs):
    app = current_app._get_current_object()
    omniliner_admin = app.config['OMNILINER_ADMIN']
    message = Message(__MESSAGE_SUBJECT, sender=omniliner_admin, recipients=[omniliner_admin])
    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', **kwargs)
    mail.send(message)