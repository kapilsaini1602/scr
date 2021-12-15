from django.core.mail import send_mail
import uuid
from django.conf import settings
def send_forget_pass(email,token):


    subject = "Link of your forgot password"
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change_pass/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
