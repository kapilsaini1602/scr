from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from decimal import Decimal
from .models import *
from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from paytm_integ.models import OrderDetails
from . import Checksm


# Create your views here.
def process_payment_paypal(request):
    if request.method == "POST":
        host = request.get_host()
        username = request.POST.get('email')
        password = request.POST.get('password')
        ammount = request.POST.get('ammount')
        obj = OrderDetails.objects.create(username=username, password=password, ammount=ammount)
        obj.save()
        # order = get_object_or_404(OrderDetails, id=obj.id)
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': ammount,
            'item_name': 'Order {}'.format(obj.id),
            'invoice': str(obj.id),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host,
                                               reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('payment_done_paypal')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('payment_cancelled_paypal')),
        }
        paytm_dict = {
            'MID': 'yRKdgL21634551259403',
            'ORDER_ID': str(obj.id),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/paytm_integ/handlepayment/',
            'CUST_ID': username,
            'TXN_AMOUNT': str(ammount),
        }
        paytm_dict['CHECKSUMHASH'] = Checksm.generate_checksum(paytm_dict, 'JU78@Z_IBrWJcA30')

        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'paypal_payment.html', {'fm_paypal': form, 'fm_paytm': paytm_dict})

    return render(request, 'paypal_index.html')


def payment_done_paypal(request):
    print(request.session.keys())
    return render(request, 'payment_done_paypal.html')


def payment_cancelled_paypal(request):
    return render(request, 'payment_cancelled_paypal.html')
