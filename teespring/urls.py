from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.ProductsView.as_view()),
    path("stores/",views.StoresView.as_view()),
    path("users/",views.UsersView.as_view()),
    path("categories/",views.CategoriesView.as_view()),
]
