import requests
from django.core.mail import send_mail
import http.client
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def send_forget_password_mail(email, token):
    subject, from_email, to = 'Your forget password link', settings.EMAIL_HOST_USER, email
    text_content = 'Password reset Email'
    html_content = f'<a href="http://127.0.0.1:8000/change-password/{token}">Click here to reset your Password.</a>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_otp(number, otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.AUTH_KEY
    headers = {'content-type': "application/json"}
    url = "http://control.msg91.com/api/sendotp.php?otp=" + otp + "&message=" + "Yourotpis" + otp + "&mobile=" + number + "&authkey=" + authkey + "&country=91"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    print(data)
    return None


def send_reg_otp(contact_number, otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.AUTH_KEY
    headers = {'content-type': "application/json"}
    url = "http://control.msg91.com/api/sendotp.php?otp=" + otp + "&message=" + "Yourotpis" + otp + "&mobile=" + contact_number + "&authkey=" + authkey + "&country=91"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    print(data)
    return None





