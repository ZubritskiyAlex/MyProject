from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

from api.views import UserViewSet, StoreViewSet, CategoryViewSet, ProductViewSet, ReviewViewSet, \
    UsersProductsRelationView, UsersStoresRelationView,  OrderViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'configureStore', StoreViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'product_relation', UsersProductsRelationView)
router.register(r'store_relation', UsersStoresRelationView)

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('', include(router.urls)),

]


