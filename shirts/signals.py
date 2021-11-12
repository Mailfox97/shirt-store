from django.shortcuts import get_object_or_404
from .models import Order, User, Cart
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver

@receiver(valid_ipn_received)
def complete_order(sender, **kwargs):
    """
    Receiver function for successful payment.
    Calls when PayPal returns success.
    """
    ipn_obj = sender
    if ipn_obj.payment_status == 'Completed':
        user = None
        user_id = ipn_obj.custom_user
        order_id = ipn_obj.custom_id
        # Get the order :D
        order = get_object_or_404(Order, id=order_id)
        user = get_object_or_404(User, id=user_id)

        finalorders = order
        finalorders.order_status = 'PLACED'
        finalorders.save()
        Cart.objects.filter(user=user).delete()