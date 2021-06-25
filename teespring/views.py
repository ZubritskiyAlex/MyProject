from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView, DetailView, FormView
from teespring.models import Product, Store, User, Category
from .forms import ReviewForm, AddProductForm, AddStoreForm, AddReviewForm

menu = ["Stores","Products","Users","About app", "Create store", "Create product"]

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
#    form_class = forms.
    template_name = "products/product_detail.html"
    slug_field = "url"



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
        product = Product.objects.get(url=slug)
        return render(request, "products/product_detail.html", {"product": product})


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
    slug_field = "url"
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
            form = AddProductForm(request.user,request.POST)
            if form.is_valid():
                product = form.save()
                url = product.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AddProductForm()
        return render(request, 'products/product_create.html', {'form': form})


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


class CreateReview(DetailView):

    @login_required
    def store_create(self, request):
        if request.method == 'POST':
            form = AddStoreForm(request.user, request.POST)
            if form.is_valid():
                review = form.save()
                url = review.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AddReviewForm()
        return render(request, 'stores/store_create.html', {'form': form})


class AddReview(DetailView):
    """Feedback for product"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())
