from . import views
from django.urls import path, include

from .views import LoginView, about, main_page, CreateProduct, CreateReview, CreateStore, RegisterUserView, logout_user, \
    show_product, store_detail

urlpatterns = [

    path("searchproduct/", views.search_products, name='searchproduct'),
    path('', main_page, name='home'),
    path("products/", views.ProductsListView.as_view(), name='product_list'),
    path('about/', about, name='about'),
    path('addproduct/', CreateProduct.as_view(), name='add_product'),
    path('addstore/', CreateStore.as_view(), name='create_store'),
    path("stores/", views.StoresListView.as_view(), name='stores_list'),
    path("users/", views.UsersListView.as_view(), name='user_list'),
    path('addreview/', CreateReview.as_view(), name='create_review'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path("searchproduct/", views.search_products, name='searchproduct'),
    path("createorder/", views.OrderCreate.create_order, name='create_order'),
    path("categories/", views.CategoriesListView.as_view(), name='categories_list'),
    path("productsofstore/<int:store_id>", views.show_products_of_store, name='products_of_store'),
    path('product/<int:product_id>/', show_product, name='product'),
    path('store/<int:store_id>/', store_detail, name='store'),
    path('cart/', include('cart.urls', )),
    path('orders/', include('orders.urls')),

]

