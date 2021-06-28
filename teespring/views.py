from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from django.views.generic import ListView, DetailView
from teespring.models import Product, Store, User, Category, Order
from .forms import AddProductForm, AddStoreForm, AddReviewForm, OrderForm, LoginForm, RegistrationForm
from .mixins import CartMixin

menu = ["Stores", "Products", "Users", "About app", "Create store", "Create product"]

def index_view(request):
    return render(request, 'index.html', {'menu': menu, 'title': 'Main page'})


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
    """ProductDetailView"""

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
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get("q")}'
        return context




class StoresListView(ListView):
    """Stores list"""

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
    template_name = "users/users_list.html"
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
    slug = "slug"
    template_name = "categories/category_detail.html"
    ordering = "name"

    def get(self, request, slug):
        category = Category.objects.get(slug)
        return render(request, "categories/category_detail.html", {"category": category})


class CreateProduct(DetailView):

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
        return render(request, 'products/product_create.html', {'form': form})

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


class CreateStore(DetailView):

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


class CreateReview(DetailView):

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


class AddReview(DetailView):
    """Feedback for product"""

    def post(self, request, pk):
        form = AddReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


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
        return render(request, 'order/order_form.html', context)

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


class LoginView(CartMixin,View):

    def get(self,request,*args,**kwargs):
        form = LoginForm(request.POST or None)
        categories = Category.objects.all()
        context ={'form':form, 'categories':categories,'cart': self.cart}
        return render(request,'login.html',context)

    def post(self, request,*args,**kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
            return render(request,'login.html',{'form':form, 'cart':self.cart})


class RegistrationView(CartMixin, View):

    def get(self,request,*args,**kwargs):
        form = LoginForm(request.POST or None)
        categories = Category.objects.all()
        context ={'form':form, 'categories':categories,'cart': self.cart}
        return render(request,'registration.html',context)

    def post(self, request,*args,**kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            User.objects.create_user(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            user = authenticate(username=form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form, 'cart': self.cart}
        return render(request,'registration.html', context)

