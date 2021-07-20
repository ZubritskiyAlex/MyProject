from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from teespring.models import Product
from .cart import Cart
from .forms import CartAddProductForm


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(reverse_lazy("cart:cart_detail"))



def cart_add(request, product_id):
    cart = Cart(request)
    print(766)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})





