from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
from teespring.models import Product, Store, User, Category, Order
from .forms import AddProductForm, AddStoreForm, AddReviewForm, OrderForm, RegisterUserForm, LoginUserForm
from .mixins import menu, DataMixin
from cart.forms import CartAddProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from teespring.models import Product
from .models import Cart
from .forms import CartAddProductForm


def search_products(request):
    if request.method == 'POST':
        searched =request.POST['searched']
        products = Product.objects.filter(title__contains=searched)

        return render(request,'search/searchproduct.html',{'searched':searched,'products':products})
    else:
        return render(request, 'search/searchproduct.html',{})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product_detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
        'title': product.title,
    }
    return render(request, 'products/product.html', context=context)


def show_store(request, store_id):
    store = get_object_or_404(Store,
                                id=store_id,
                                available=True)
    return render(request, 'stores/store_detail.html')

def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    return render(request,
                  'products/product_detail.html',
                  {'product': product})


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
    queryset = Product.objects.all()
    template_name = "products/product_list.html"
    ordering_fields = ['price', 'title', 'category ', 'description']

    def get(self,request):
        products = Product.objects.all()
        return render(request, "products/product_list.html", {"product_list": products})

class ProductDetailView(DetailView):

    model = Product
    template_name = "products/product_detail.html"
    slug_field = "title"

    def get_success_url(self):
        return reverse('products:detail', args=[self.kwargs['slug'], self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['events'] = self.object.events.all()
        return context

    def get_form_kwargs(self):
        kwargs = super(ProductDetailView, self).get_form_kwargs()
        kwargs['product_pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        form.send_download_links()
        return super(ProductDetailView, self).form_valid(form)



    def get(self, request, slug):
        product = Product.objects.get(slug)
        return render(request, "products/product_detail.html", {"product": product})


class SearchProducts(ListView):
    "Search products"
    template_name = 'search/search.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('s'))


    def get_context_data(self, *args,object_list=None , **kwargs):
        context = super().get_context_data( **kwargs)
        context['s'] = f's={self.request.GET.get("s")}&'
        return context




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


class StoreDetailView(DetailView):
    """StoreDetailView """

    model = Store
    slug_field = "name"
    template_name = "stores/store_detail.html"

    def get(self, request, slug):
        store = Store.objects.get(slug)
        return render(request, "stores/store_detail.html", {"store": store})



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

class UserDetailViewSet(DetailView):
    """UserDetailView """

    model = User
    slug_field = "username"
    template_name = "users/user_detail.html"

    def get(self, request, slug):
        user = User.objects.get(slug)
        return render(request, "users/user_detail.html", {"user": user})


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
    slug_url_kwarg = "slug"
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
    queryset = Product.objects.filter(stores=store_id)
    context = {
        'products': queryset,
        'title': queryset.title,
    }
    return render(request, 'products/products_of_store.html', context=context)
