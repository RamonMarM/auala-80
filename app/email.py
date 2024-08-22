from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail
import requests

import requests
from datetime import datetime

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])    
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox59e2363bd1af4261b42440f4c044d44a.mailgun.org/messages",
  		auth=("api", "8a399a332e3d31c60c580ba9e43d8927-2b91eb47-b8117fdb"),
  		data={"from": "Ramon Martins <mailgun@sandbox59e2363bd1af4261b42440f4c044d44a.mailgun.org>",
  			"to": ["ramonmendoncapiu@gmail.com"],
  			"subject": "Envio de email avaliacao 80",
  			"text": "Teste Teste Teste!"})