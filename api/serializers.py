from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from teespring.models import User, Store, Product, Category, Review, UsersProductsRelation, UsersStoresRelation


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    annotataed_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Store
        fields = '__all__'

    def get_likes_count(self, instance):
        return UsersStoresRelation.objects.filter(store=instance, like=True).count()


class ProductSerializer(ModelSerializer):

    likes_count = serializers.SerializerMethodField()
    annotataed_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2,read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_likes_count(self, instance):
        return UsersProductsRelation.objects.filter(product=instance, like=True).count()


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UsersProductsRelationSerializers(ModelSerializer):
    class Meta:
        model = UsersProductsRelation
        fields = '__all__'


class UsersStoresRelationSerializers(ModelSerializer):
    class Meta:
        model = UsersStoresRelation
        fields = '__all__'
