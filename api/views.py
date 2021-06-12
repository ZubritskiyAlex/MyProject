from rest_framework.viewsets import ModelViewSet
from api.pagination import CustomPageNumberPagination
from api.permissions import IsOwnerStaffOrReadOnly
from api.serializers import UserSerializer, StoreSerializer, CategorySerializer, ProductSerializer, ReviewSerializer
from teespring.models import User, Store, Category, Product, Review
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
#    permission_classes = [IsAuthenticated]
    filter_fields = ['username', 'first_name', "last_name", "email", "description", "is_owner"]
    search_fields = ['username', 'is_owner', 'email', "description"]


class StoreViewSet(ModelViewSet):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerStaffOrReadOnly]
    filter_fields = ['name', 'description']
    search_fields = ['popular_product', 'tranding_category']


    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    filter_fields = ['name', 'slug', 'url']
    search_fields = ['name', 'url']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['title', 'stores', 'category']
    permission_classes = [IsOwnerStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
#   search_fields = ("title", "content")

