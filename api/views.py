from django.conf.urls import url
from django.db.models import Count, Case, When, Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from api.pagination import CustomPageNumberPagination
from api.permissions import IsOwnerStaffOrReadOnly
from api.serializers import UserSerializer, StoreSerializer, CategorySerializer, ProductSerializer, ReviewSerializer, \
    UsersProductsRelationSerializers, UsersStoresRelationSerializers, CartSerializer, CartProductSerializer, \
    OrderSerializer
from api.utils import get_cart_and_products_in_cart
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from teespring.models import User, Store, Category, Product, Review, \
    UsersStoresRelation, UsersProductsRelation, Cart, CartProduct, Order
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth import authenticate

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'}, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'Could not login. Please check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=200)


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

    #queryset = UsersStoresRelation.objects.filter(like=True)
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
    queryset = Product.objects.all().annotate(annotate_likes=Count(Case(When(usersproductsrelation__like=True, then=1))),
                                                  rating=Avg('usersproductsrelation__rate')).order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['title', 'shops', 'category']
    permission_classes = [IsOwnerStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        cart, products_in_cart = get_cart_and_products_in_cart(request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            serializer_data = serializer.data
            if cart:
                for product in serializer_data:
                    product['in_cart'] = True if product['id'] in products_in_cart else False
            return self.get_paginated_response(serializer_data)

        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        if cart:
            for product in serializer_data:
                product['in_cart'] = True if product['id'] in products_in_cart else False
        return Response(serializer_data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cart, products_in_cart = get_cart_and_products_in_cart(request)
        serializer_data = serializer.data
        if cart:
            serializer_data['in_cart'] = False if instance.id not in products_in_cart else True
        return Response(serializer_data)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
#   search_fields = ("title", "content")


class UsersProductsRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UsersProductsRelation.objects.all()
    serializer_class = UsersProductsRelationSerializers
    lookup_field = 'product'

    def get_object(self):
        obj, created = UsersProductsRelation.objects.get_or_create(
                    user=self.request.user,
                    product_id=self.kwargs['product'])
        return obj


class UsersStoresRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UsersStoresRelation.objects.all()
    serializer_class = UsersStoresRelationSerializers
    lookup_field = 'store'

    def get_object(self):
        obj, created = UsersProductsRelation.objects.get_or_create(
                    user=self.request.user,
                    product_id=self.kwargs['store'])
        return obj



class CartViewSet(ModelViewSet):

    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    @staticmethod
    def get_cart(user):
        if user.is_authenticated:
            return Cart.objects.filter(owner=user.customer, for_anonymous_user=False).first()
        return Cart.objects.filter(for_anonymous_user=True).first()

    @staticmethod
    def _get_or_create_cart_product(user:User , cart: Cart, product: Product):
        cart_product, created = CartProduct.objects.get_or_create(
            user=user,
            product=product,
            cart=cart
        )
        return cart_product, created

    @action(methods=["get"], detail=False)
    def current_customer_cart(self, *args, **kwargs):
        cart = self.get_cart(self.request.user)
        cart_serializer = CartSerializer(cart)
        return Response(cart_serializer.data)

    @action(methods=['put'], detail=False, url_path='current_customer_cart/add_to_cart/(?P<product_id>\d+)')
    def product_add_to_cart(self, *args, **kwargs):
        cart = self.get_cart(self.request.user)
        product = get_object_or_404(Product, id=kwargs['product_id'])
        cart_product, created = self._get_or_create_cart_product(self.request.user.customer, cart, product)
        if created:
            cart.products.add(cart_product)
            cart.save()
            return Response({"detail": "Товар добавлен в корзину", "added": True})
        return Response({'detail': "Товар уже в корзине", "added": False}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["patch"], detail=False, url_path='current_customer_cart/change_qty/(?P<qty>\d+)/(?P<cart_product_id>\d+)')
    def product_change_qty(self, *args, **kwargs):
        cart_product = get_object_or_404(CartProduct, id=kwargs['cart_product_id'])
        cart_product.qty = int(kwargs['qty'])
        cart_product.save()
        cart_product.cart.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=["put"], detail=False, url_path='current_customer_cart/remove_from_cart/(?P<cproduct_id>\d+)')
    def product_remove_from_cart(self, *args, **kwargs):
        cart = self.get_cart(self.request.user)
        cproduct = get_object_or_404(CartProduct, id=kwargs['cproduct_id'])
        cart.products.remove(cproduct)
        cproduct.delete()
        cart.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartProductViewSet(ModelViewSet):

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title", "content")


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("first_name", "last_name", "address", "created_at", "order_date",)

