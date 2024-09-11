from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Pxkk3Iv1u4He6M8uv4haokMkbbyT48WxZ0tZ9DPPgADAShnLN648hJi8iXMwFYcMECIkd6CvuPYYr4X7OcElGrN00NcXVSjNa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)