from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.ProductsView.as_view()),
    path("stores/",views.StoresView.as_view()),
    path("users/",views.UsersView.as_view()),
    path("categories/",views.CategoriesView.as_view()),
    path("product/", views.ProductDetailView.as_view(), name='product_detail'),
    path("<store>/", views.StoreDetailView.as_view(), name='store_detail'),
    path("<user>/", views.UserDetailView.as_view(), name='user_detail'),
    path("<category>/", views.CategoryDetailView.as_view(), name='category_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),


]
