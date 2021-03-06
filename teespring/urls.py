from . import views
from django.urls import path, include

from .views import LoginView, about, main_page, CreateProduct, CreateReview, CreateStore, RegisterUserView, logout_user, \
    ProductDetailView, show_product

urlpatterns = [
    path("products/", views.ProductsListView.as_view(), name='product_list'),
    path('product/<int:product_id>/', show_product, name='product'),
    path('', main_page, name='home'),
    path('about/', about, name='about'),
    path('addproduct/', CreateProduct.as_view(), name='add_product'),
    path('addstore/', CreateStore.as_view(), name='create_store'),

    path("stores/", views.StoresListView.as_view(), name='stores_list'),
    path("users/", views.UsersListView.as_view(), name='user_list'),
    path('addreview/', CreateReview.as_view(), name='create_review'),
    path("categories/", views.CategoriesListView.as_view(), name='categories_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path("product/<int:product_id>/", views.product_detail, name='product_detail'),
    # path("product/<int:product_id>/", views.product_detail, name='product_detail'),
    path("store/<int:store_id>", views.show_store, name='store'),
    path('cart/', include('cart.urls', )),
    path('orders/', include('orders.urls')),
    path("createorder/", views.OrderCreate.create_order, name='create_order'),
    path("searchproduct/", views.search_products, name='searchproduct'),
    path('productdetail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:product_id>/', show_product, name='product'),





#path('search_stores/',views.SearchStores.as_view(), name='search_stores'),
#path("<user>/", views.UserDetailViewSet.as_view(), name='user_detail'),
#path("update_order/<str:pk>/", views.OrderCreate.update_order, name='update_order'),
#path("delete_order/<str:pk>/", views.OrderCreate.delete_order, name='delete_order'),
#path("update_store/<str:pk>/", views.CreateStore.update_store, name='update_store'),
#path("delete_store/<str:pk>/", views.CreateStore.delete_store, name='delete_store'),
#    path("update_product/<str:pk>/", views.CreateProduct.update_product, name='update_product'),
#    path("delete_product/<str:pk>/", views.CreateProduct.delete_product, name='delete_product'),
#    path("create_review/", views.CreateReview.review_create, name='create_review'),
#    path("update_review/<str:pk>/", views.CreateReview.review_update, name='update_review'),
#    path("delete_review/<str:pk>/", views.CreateReview.delete_review, name='delete_review'),

]
