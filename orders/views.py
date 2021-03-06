from django.shortcuts import render
from cart.models import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from MyProject.tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear basket
            cart.clear()
            # start asynchronous tasks
            #order_created.delay(order.id)
            return render(request, 'orders/order/create.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
