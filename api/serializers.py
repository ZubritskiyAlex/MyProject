from rest_framework.serializers import ModelSerializer

from teespring.models import User, Store, Product, Category, Review, UserProductRelation, UserStoreRelation


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UserProductRelationSerializers(ModelSerializer):
    class Meta:
        model = UserProductRelation
        fields = '__all__'


class UserStoreRelationSerializers(ModelSerializer):
    class Meta:
        model = UserStoreRelation
        fields = '__all__'

