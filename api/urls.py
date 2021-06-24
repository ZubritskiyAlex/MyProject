from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, StoreViewSet, CategoryViewSet, ProductViewSet, ReviewViewSet, \
    UsersProductsRelationView, UsersStoresRelationView

router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'store', StoreViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'product_relation', UsersProductsRelationView)
router.register(r'store_relation', UsersStoresRelationView)


urlpatterns = router.urls

