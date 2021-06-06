from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import DetailView, ListView

from teespring.models import Product, Store, User, Category
from .forms import ReviewForm, AddProductForm, AddStoreForm


class ProductsView(ListView):
    """Products list"""

    model = Product
    queryset = Product.objects.all()
    template_name = "products/product_list.html"

#    def get(self,request):
#        products = Product.objects.all()
#        return render(request, "products/product_list.html", {"product_list": products})

class ProductDetailView(DetailView):
    """ProductDetailView"""

    model = Product
    slug_field = "url"

#    def get(self, request, slug):
#        product = Product.objects.get(url=slug)
#        return render(request, "products/product_detail.html", {"product": product})


class StoresView(ListView):
    """Stores list"""
    model = Store
    queryset = Store.objects.all()
    template_name = "stores/stores_list.html"


#    def get(self, request):
#        stores = Store.objects.all()
#        return render(request, "stores/stores_list.html", {"store_list": stores})

class StoreDetailView(DetailView):
    """StoreDetailView """

    model = Store
    slug_field = "url"


#    def get(self, request, slug):
#        store = Store.objects.get(slug)
#        return render(request, "stores/store_detail.html", {"store": store})


class UsersView(ListView):
    """Users list"""

    model = User
    queryset = User.objects.all()
    template_name = "users/user_list.html"


#    def get(self, request):
#        users = User.objects.all()
#        return render(request, "users/user_list.html", {"user_list": users})

class UserDetailView(DetailView):
    """UserDetailView """

    model = User
    slug_field = "url"

#    def get(self, request, slug):
#        user = User.objects.get(slug)
#        return render(request, "users/user_detail.html", {"user": user})


class CategoriesView(ListView):
    """Categories list"""

    model = Category
    queryset = Category.objects.all()
    template_name = "categories/categories_list.html"

#    def get(self, request):
#        categories = Category.objects.all()
#        return render(request, "categories/categories_list.html", {"categories_list": categories})


class CategoryDetailView(View):
    """CategoryDetailView """

    model = User
    slug_field = "url"

#    def get(self, request, slug):
#        category = Category.objects.get(slug)
#        return render(request, "users/user_detail.html", {"category": category})

class AddReview(View):
    """Feedback for product"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


class CreateProduct(View):

    @login_required
    def product_create(self, request):
        if request.method == 'POST':
            form = AddProductForm(request.user,request.POST)
            if form.is_valid():
                product = form.save()
                url = product.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AddProductForm()
        return render(request, 'products/product_create.html', {'form': form})


class CreateStore(View):

    @login_required
    def store_create(self, request):
        if request.method == 'POST':
            form = AddStoreForm(request.user, request.POST)
            if form.is_valid():
                store = form.save()
                url = store.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AddStoreForm()
        return render(request, 'stores/store_create.html', {'form': form})



