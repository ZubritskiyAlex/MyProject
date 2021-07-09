from django.contrib.auth import login
from django.contrib.auth.views import LogoutView

from . import views
from django.urls import path

from .views import LoginView, about, main_page, CreateProduct, CreateReview, CreateStore, RegisterUserView, logout_user

urlpatterns = [

    path('', main_page, name='home'),
    path('about/', about, name='about'),
    path('addproduct/', CreateProduct.as_view(), name='add_product'),
    path('addstore/', CreateStore.as_view(), name='create_store'),
    path("products/", views.ProductsListView.as_view(), name='product_list'),
    path("stores/", views.StoresListView.as_view(), name='stores_list'),
    path("users/", views.UsersListView.as_view(), name='user_list'),
    path('addreview/', CreateReview.as_view(), name='create_review'),
    path("categories/", views.CategoriesListView.as_view(), name='categories_list'),
    path('login/',LoginView.as_view(), name ='login'),
    path('register/',RegisterUserView.as_view(), name='register'),
    path('logout/',logout_user, name='logout'),
    path("product/<int:product_id>/", views.show_product, name='product_detail'),
    path("store/<int:store_id>", views.show_store, name='store'),

    #    path('search_stores/',views.SearchStores.as_view(), name='search_stores'),
#    path('search_products/',views.SearchProducts.as_view(), name='search_products'),

#    path("<user>/", views.UserDetailViewSet.as_view(), name='user_detail'),
#    path("<category>/", views.CategoryDetailView.as_view(), name='category_detail'),
#    path("create_order/",views.OrderCreate.create_order, name='create_order'),
#    path("update_order/<str:pk>/", views.OrderCreate.update_order, name='update_order'),
#    path("delete_order/<str:pk>/", views.OrderCreate.delete_order, name='delete_order'),

#    path("update_store/<str:pk>/", views.CreateStore.update_store, name='update_store'),
#    path("delete_store/<str:pk>/", views.CreateStore.delete_store, name='delete_store'),

#    path("update_product/<str:pk>/", views.CreateProduct.update_product, name='update_product'),
#    path("delete_product/<str:pk>/", views.CreateProduct.delete_product, name='delete_product'),
#    path("create_review/", views.CreateReview.review_create, name='create_review'),
#    path("update_review/<str:pk>/", views.CreateReview.review_update, name='update_review'),
#    path("delete_review/<str:pk>/", views.CreateReview.delete_review, name='delete_review'),




]
