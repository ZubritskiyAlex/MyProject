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


#path('productssort/', products_list, name='product_list'),
    path('cart/', include('cart.urls', )),
    path('orders/', include('orders.urls')),
#path('cart/',views.cart, name='cart'),
#path('checkout/',views.checkout, name='checkout'),
#path('update_item/',views.updateItem, name='update_item'),
#path('cartadd/', views.cart_add, name='cart_add'),

]

#path("<user>/", views.UserDetailViewSet.as_view(), name='user_detail'),
#path("update_order/<str:pk>/", views.OrderCreate.update_order, name='update_order'),
#path("delete_order/<str:pk>/", views.OrderCreate.delete_order, name='delete_order'),
#path("update_store/<str:pk>/", views.CreateStore.update_store, name='update_store'),
#path("delete_store/<str:pk>/", views.CreateStore.delete_store, name='delete_store'),
