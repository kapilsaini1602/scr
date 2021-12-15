from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', process_payment_paypal, name='process_payment_paypal'),
    path('payment-done-paypal/', payment_done_paypal, name='payment_done_paypal'),
    path('payment-cancelled-paypal/', payment_cancelled_paypal, name='payment_cancelled_paypal'),
]
