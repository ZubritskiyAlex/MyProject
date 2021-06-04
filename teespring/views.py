from django.shortcuts import render

# Create your views here.
from django.views import View

from teespring.models import Product, Store, User


class ProductsView(View):

    def get(self,request):
        products = Product.objects.all()
        return render(request, "products/product_list.html", {"product_list": products})


class StoresView(View):

    def get(self,request):
        stores = Store.objects.all()
        return render(request, "stores/stores_list.html", {"store_list": stores})


class UsersView(View):

    def get(self, request):
        users = User.objects.all()
        return render(request, "users/user_list.html", {"user_list": users})

class CategoriesView(View):

    def get(self, request):
        stores = Store.objects.all()
        return render(request, "categories/categories_list.html", {"category_list": stores})



