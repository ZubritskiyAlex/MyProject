import json
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from resevation.forms import ReservationForm
from teespring.models import Store, User, Category, Order, OrderItem
from .forms import AddProductForm, AddStoreForm, AddReviewForm, OrderForm, RegisterUserForm, LoginUserForm
from .mixins import menu, DataMixin
from django.shortcuts import render, redirect, get_object_or_404
from teespring.models import Product


def search_products(request):
    if request.method == 'POST':
        searched =request.POST['searched']
        products = Product.objects.filter(title__contains=searched)

        return render(request,'search/searchproduct.html',{'searched':searched,'products':products})
    else:
        return render(request, 'search/searchproduct.html',{})

def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    return render(request, "stores/store.html", {'store':store})


def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReservationForm(request.POST or None, initial={"product": product})
    context = {
        'product': product,
        'title': product.title,
        'form': form,
        'sended':request.GET.get("sended", False),
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=True".format(reverse('product', kwargs={"product_id":product_id})))

    return render(request, 'products/product.html', context=context)


def show_store(request, store_id):
    store = get_object_or_404(Store,
                                pk=store_id)
    context = {
        'store': store,
        'name': store.name,
    }

    return render(request, 'stores/store_detail.html', context=context)




def main_page(request):
    stores = Store.objects.all()
    return render(request, 'main.html',{'stores':stores, 'title':'Main page!'})

def about(request):
    contact_list = Store.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'about.html', {'page_obj':page_obj,'menu': menu,'title': 'About app'})


class ProductsListView(ListView):
    """Products list"""

    model = Product
    template_name = "products/product_list.html"
    ordering_fields = ['price', 'title', 'category ', 'description']


class StoresListView(ListView):
    """Stores list"""
    paginate_by = 5
    model = Store
    queryset = Store.objects.all()
    template_name = "stores/stores_list.html"
    ordering_fields = ['name', 'description', 'popular_product']


    def get(self, request):
        stores = Store.objects.all()
        return render(request, "stores/stores_list.html", {"store_list": stores})


class SearchStores(ListView):
    "Search stores"
    paginate_by = 5

    def get_queryset(self):
        return Store.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['q'] = f'q={self.request.GET.get("q")}'
        return context



class UsersListView(ListView):
    """Users list"""

    model = User
    queryset = User.objects.all()
    template_name = "users/user_list.html"
    ordering_fields = ['username', 'is_owner', 'email']


    def get(self, request):
        users = User.objects.all()
        return render(request, "users/user_list.html", {"user_list": users})



class CategoriesListView(ListView):
    """Categories list"""

    model = Category
    queryset = Category.objects.all()
    ordering_fields = ['name', 'url', 'slug']
    template_name = "categories/categories_list.html"

    def get(self, request):
        categories = Category.objects.all()
        return render(request, "categories/categories_list.html", {"categories_list": categories})


class CategoryDetailView(DetailView):
    """CategoryDetailView """

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = "categories/category_detail.html"


class CreateProduct(LoginRequiredMixin, CreateView):

    form_class = AddProductForm
    template_name = 'products/addproduct.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(CreateProduct, self).get_context_data(**kwargs)
        context['title'] = "Add product"
        context['menu'] = menu
        return context

    @login_required
    def product_create(self, request):
        if request.method == 'POST':
            form = AddProductForm(request.user, request.POST)
            if form.is_valid():
                product = form.save()
                url = product.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AddProductForm()
        return render(request, 'products/addproduct.html', {'form': form})

    @login_required()
    def update_product(request, pk):

        product = Product.objects.get(id=pk)
        form = AddProductForm(instance=product)

        if request.method == 'POST':
            form = AddProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form': form}
        return render(request, 'products/product_update.html', context)

    @login_required()
    def delete_product(request, pk):
        product = Product.objects.get(id=pk)
        if request.method == 'POST':
            product.delete()
            return redirect('/')

        context = {'item': product}
        return render(request, 'products/product_delete.html', context)


class CreateStore(LoginRequiredMixin, CreateView):

    form_class = AddStoreForm
    template_name = 'stores/store_create.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(CreateStore, self).get_context_data(**kwargs)
        context['title'] = "Add store!"
        context['menu'] = menu
        return context

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

    @login_required
    def update_store(request, pk):

        store = Store.objects.get(id=pk)
        form = AddStoreForm(instance=store)

        if request.method == 'POST':
            form = AddStoreForm(request.POST, instance=store)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form': form}
        return render(request, 'stores/store_update.html', context)

    @login_required
    def delete_store(request, pk):
        store = Store.objects.get(id=pk)
        if request.method == 'POST':
            store.delete()
            return redirect('/')

        context = {'item': store}
        return render(request, 'stores/store_delete.html', context)


class AddReview(LoginRequiredMixin, CreateView):
    """Feedback for product"""

    def post(self, request, pk):
        form = AddReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())

class CreateReview(LoginRequiredMixin, CreateView):

    form_class = AddReviewForm
    template_name = 'review/review_create.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    @login_required
    def review_create(self, request):
        if request.method == 'POST':
            form = AddReviewForm(request.user, request.POST)
            if form.is_valid():
                review = form.save()
                url = review.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AddReviewForm()
        return render(request, 'review/review_create.html', {'form': form})

    @login_required
    def review_update(request, pk):

        review = AddReview.objects.get(id=pk)
        form = AddReviewForm(instance=review)

        if request.method == 'POST':
            form = AddReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form': form}
        return render(request, 'review/review_update.html', context)

    @login_required
    def delete_review(request, pk):
        review = AddReviewForm.objects.get(id=pk)
        if request.method == 'POST':
            review.delete()
            return redirect('/')

        context = {'item': review}
        return render(request, 'review/review_delete.html', context)



class OrderCreate(DetailView):
    '''CRUD ORDER'''
    def create_order(request):

        form = OrderForm()
        if request.method =='POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form':form}
        return render(request, 'orders/order/create.html', context)

    def update_order(request,pk):

        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)

        if request.method =='POST':
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form': form}
        return render(request,'order/order_form.html', context)

    def delete_order(request, pk):
        order = Order.objects.get(id=pk)
        if request.method == 'POST':
            order.delete()
            return redirect('/')

        context = {'item': order}
        return render(request, 'order/delete_order.html', context)


class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/../templates/registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ViewProduct(DetailView):
    model = Product
    pk_url_kwarg = 'product_id'
    template_name = 'products/product_detail.html'
    context_object_name = 'product_item'


def show_products_of_store(request, store_id):
    product = Product.objects.filter(product__id=store_id)
    context = {
        'products': product,
        'title': product.title,
    }
    return render(request, 'products/products_of_store.html', context=context)







#####deni ivy

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'shop/shop.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'shop/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)



####
