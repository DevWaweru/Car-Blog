from flask_mail import Message
# from manage import app
from . import mail
from flask import render_template
import os

def send_email(subject, sender, recepients, text_body, html_body):
    msg = Message(subject,sender=sender,recipients=recepients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_subscriptions(new_subscription):
    send_email('Subscribed to BeauCars Blog',sender=os.environ.get('MAIL_USERNAME'),recepients=[new_subscription.email_data],text_body=render_template('emails/subscribed.txt', new_subscription=new_subscription),html_body=render_template('emails/subscribed.html', new_subscription=new_subscription))

# def send_blogs(user)