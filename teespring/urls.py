from . import views
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("products/", views.ProductsListView.as_view(), name='product_list'),
    path("stores/", views.StoresListView.as_view(), name='stores_list'),
    path("users/", views.UsersListView.as_view(), name='user_list'),
    path("categories/", views.CategoriesListView.as_view(), name='categories_list'),
    path("product/", views.ProductDetailView.as_view(), name='product_detail'),
    path("<store>/", views.StoreDetailView.as_view(), name='store_detail'),
    path("<user>/", views.UserDetailViewSet.as_view(), name='user_detail'),
    path("<category>/", views.CategoryDetailView.as_view(), name='category_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("create_order/",views.OrderCreate.create_order, name='create_order'),
    path("update_order/<str:pk>/", views.OrderCreate.update_order, name='update_order'),
    path("delete_order/<str:pk>/", views.OrderCreate.delete_order, name='delete_order'),

    path("create_store/",views.CreateStore.store_create, name='create_store'),
    path("update_store/<str:pk>/", views.CreateStore.update_store, name='update_store'),
    path("delete_store/<str:pk>/", views.CreateStore.delete_store, name='delete_store'),

    path("create_product/",views.CreateProduct.product_create, name='create_product'),
    path("update_product/<str:pk>/", views.CreateProduct.update_product, name='update_product'),
    path("delete_product/<str:pk>/", views.CreateProduct.delete_product, name='delete_product'),

    path("create_review/", views.CreateReview.review_create, name='create_review'),
    path("update_review/<str:pk>/", views.CreateReview.review_update, name='update_review'),
    path("delete_review/<str:pk>/", views.CreateReview.delete_review, name='delete_review')
]
