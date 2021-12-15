from paytm_integ.models import OrderDetails
from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        order = OrderDetails.objects.get(id=ipn.invoice)
        if order.ammount == ipn.mc_gross:
            # mark the order as paid
            order.payment_status = True
            order.save()
