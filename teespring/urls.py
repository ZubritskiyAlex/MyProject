from django.urls import path
from . import views


urlpatterns = [
    path("products/",views.ProductsListView.as_view(), name='product_list'),
    path("stores/",views.StoresListView.as_view(), name='stores_list'),
    path("users/",views.UsersListView.as_view(), name='user_list'),
    path("categories/",views.CategoriesListView.as_view(),'categories_list'),
    path("product/", views.ProductDetailView.as_view(), name='product_detail'),
    path("<store>/", views.StoreDetailView.as_view(), name='store_detail'),
    path("<user>/", views.UserDetailViewSet.as_view(), name='user_detail'),
    path("<category>/", views.CategoryDetailView.as_view(), name='category_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),

]


#from user_profile import views

#urlpatterns = [
#    path("<str:username>/", views.UserDetailView.as_view(), name="user-profile"),
#    path("<str:username>/edit/", views.UserUpdateView.as_view(), name="edit-profile"),
#    path(
#        "<str:username>/delete/", views.UserDeleteView.as_view(), name="delete-profile"
#    ),
#]