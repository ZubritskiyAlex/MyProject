from django.urls import path

from . import views


urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cartadd/', views.cart_add, name='cart_add'),
    path('cartremove/', views.cart_remove, name='cart_remove'),
]
