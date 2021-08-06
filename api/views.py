from django.db.models import Count, Case, When, Avg
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from api.pagination import CustomPageNumberPagination
from api.permissions import IsOwnerStaffOrReadOnly
from api.serializers import UserSerializer, StoreSerializer, CategorySerializer, ProductSerializer, ReviewSerializer, \
    UsersProductsRelationSerializers, UsersStoresRelationSerializers,\
    OrderSerializer

from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from teespring.models import User, Store, Category, Product, Review, \
    UsersStoresRelation, UsersProductsRelation, Order
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

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerStaffOrReadOnly]
    filter_fields = ['name', 'description']
    search_fields = ['title', 'stores', 'category']

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



class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








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



class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("first_name", "last_name", "address", "created_at", "order_date",)

