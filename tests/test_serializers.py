from unittest import TestCase

from django.db.models import When, Count, Case, Avg

from api.serializers import ProductSerializer, UserSerializer, StoreSerializer, ReviewSerializer
from teespring.models import Product, User, Store, Category, Review, UsersProductsRelation, UsersStoresRelation


class ProductSerializerTestCase(TestCase):

    def test_ok(self):
        user_1 = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,
                                     first_name="Alexander",
                                     last_name="Zubritskiy", url="https://dagadf.com", description="asafasfc",
                                     image=None,
                                     date_created="26.04.2000", is_owner=False,
                                     )
        user_2 = User.objects.create(username="Zekych", email="axvabc@gmail.com", is_staff=False,
                                     first_name="Zeka",
                                     last_name="Zekov", url="https://dagzdafadf.com", description="axzvvsafasfc",
                                     image=None,
                                     date_created="27.02.2005", is_owner=False,
                                     )
        product_1 = Product.objects.create(title="Phone", stores="TechnoStore", category="Digital", description="Devices Store",
                                           price="500.00", date_created="01.09.2003", is_tranding_category=True,
                                           image=None, url="https://mi-shop.by/", draft=False,
                                           )
        product_2 = Product.objects.create(title="Hoodie", stores="Bershka", category="clothes", description="Сlothes configureStore",
                                           price="250.00", date_created="11.07.2005", is_tranding_category=True,
                                           image=None, url="https://www.bershka.com/", draft=False,

                                       )
        UsersProductsRelation.objects.create(user=user_1, product=product_1, like=True,rate=4)
        UsersProductsRelation.objects.create(user=user_2, product=product_1, like=True,rate=4)
        UsersProductsRelation.objects.create(user=user_1, product=product_2, like=True,rate=5)
        UsersProductsRelation.objects.create(user=user_2, product=product_2, like=True,rate=5)

        products = Product.objects.all().annotate(annotated_likes=Count(Case(When(usersproductsrelation__like=True, then=1))),
                                                  rating=Avg('usersproductsrelation__rate'))
        data = ProductSerializer(products, many=True)
        expected_data = [
            {
                'title': product_1.title,
                'shops': product_1.stores,
                'category': product_1.category,
                'description': product_1.description,
                'price': product_1.price,
                'date_created': product_1.date_created,
                'is_tranding_category': product_1.is_tranding_category,
                'image': product_1.image,
                'url': product_1.url,
                'draft': product_1.draft,
                'likes_count': 1,
                'annotated_likes': 1,
                'rating': 4
                    },

            {
                'title': product_2.title,
                'shops': product_2.stores,
                'category': product_2.category,
                'description': product_2.description,
                'price': product_2.price,
                'date_created': product_2.date_created,
                'is_tranding_category': product_2.is_tranding_category,
                'image': product_2.image,
                'url': product_2.url,
                'draft': product_2.draft,
                'likes_count': 1,
                'annotated_likes': 1,
                'rating': 5
            }
        ]
        self.assertEqual(expected_data, data)


class UserSerializerTestCase(TestCase):

    def test_ok(self):
        user_1 = User.objects.create(username ="Alex",email ="abc@gmail.com",is_staff =False,
                                     first_name = "Alexander",
                                     last_name="Zubritskiy",url ="https://dagadf.com",description ="asafasfc",image =None,
                                     date_created="26.04.2000",is_owner =False,
                                     )
        user_2 = User.objects.create(username ="Zekych",email ="axvabc@gmail.com",is_staff =False,
                                     first_name = "Zeka",
                                     last_name="Zekov",url ="https://dagzdafadf.com",description ="axzvvsafasfc",image =None,
                                     date_created="27.02.2005",is_owner =False,
                                     )

        data = UserSerializer([user_1, user_2], many=True)
        expected_data = [
            {
                'username': user_1.username,
                'email': user_1.email,
                'is_staff': user_1.is_staff,
                'first_name': user_1.first_name,
                'last_name': user_1.last_name,
                'url': user_1.url,
                'description': user_1.description,
                'image': user_1.image,
                'date_created': user_1.date_created,
                'is_owner': user_1.is_owner,
                    },

            {'username': user_2.username,
                'email': user_2.email,
                'is_staff': user_2.is_staff,
                'first_name': user_2.first_name,
                'last_name': user_2.last_name,
                'url': user_2.url,
                'description': user_2.description,
                'image': user_2.image,
                'date_created': user_2.date_created,
                'is_owner': user_2.is_owner,

            },
        ]
        self.assertEqual(expected_data, data)


class StoreSerializerTestCase(TestCase):

    def test_ok(self):
        user_1 = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,
                                     first_name="Alexander",
                                     last_name="Zubritskiy", url="https://dagadf.com", description="asafasfc",
                                     image=None,
                                     date_created="26.04.2000", is_owner=False,
                                     )
        user_2 = User.objects.create(username="Zekych", email="axvabc@gmail.com", is_staff=False,
                                     first_name="Zeka",
                                     last_name="Zekov", url="https://dagzdafadf.com", description="axzvvsafasfc",
                                     image=None,
                                     date_created="27.02.2005", is_owner=False,
                                     )
        store_1 = Store.objects.create(user= "Petr", name="TechnoStore", url="https://dagzdaqwdaf.com",
                                       description="Devices shop",
                                       tranding_category="Digital", popular_product='Staple Tee',
                                       date_created="27.02.1993", image=None,
                                       )
        store_2 = Store.objects.create(user= "Zeka", name="TechnoStore", url="https://dagzdaqwdaf.com",
                                       description ="Devices shop",
                                       tranding_category="Clothes",popular_product='Face mask',
                                       date_created="27.02.1990", image=None,
                                       )
        UsersStoresRelation.objects.create(user=user_1, product=store_1,like=True, rate=5)
        UsersStoresRelation.objects.create(user=user_2, product=store_1,like=True, rate=5)
        UsersStoresRelation.objects.create(user=user_1, product=store_2,like=True, rate=4)
        UsersStoresRelation.objects.create(user=user_2, product=store_2,like=True, rate=4)
        data = StoreSerializer([store_1, store_2], many=True)
        expected_data = [
            {
                'user': store_1.user,
                'name': store_1.name,
                'url': store_1.url,
                'description': store_1.description,
                'tranding_category':store_1.tranding_category,
                'popular_product':store_1.popular_product,
                'date_created':store_1.date_created,
                'image':store_1.image,
                'likes_count': 1,
                'rating': 5
                    },

            {
                'user': store_2.user,
                'name': store_2.name,
                'url': store_2.url,
                'description': store_2.description,
                'tranding_category': store_2.tranding_category,
                'popular_product': store_2.popular_product,
                'date_created': store_2.date_created,
                'image': store_2.image,
                'likes_count': 1,
                'rating': 4

            },
        ]
        self.assertEqual(expected_data, data)


class CategorySerializerTestCase(TestCase):

    def test_ok(self):
        category_1 = Category.objects.create(name ="Digital",slug='digit', url='https://dagzdaqasfwdaf.com',)
        category_2 = Category.objects.create(name ="Clothes",slug="wear", url='https://dqwfaxvf.com',)
        data = ProductSerializer([category_1, category_2], many=True)
        expected_data = [
            {
                'name': category_1.name,
                'slug': category_1.slug,
                'url': category_1.url

                    },

            {
                'name': category_2.name,
                'slug': category_2.slug,
                'url': category_2.url

            },
        ]
        self.assertEqual(expected_data, data)


class ReviewSerializerTestCase(TestCase):
    def test_ok(self):
        review_1 = Review.objects.create(email ='sdgba@gmail.com',name ='Alex',
                                         text ='Best configureStore in the world!',
                                         parent ='Alex',
                                         review_on_store ='Techno',product='Phone',)
        review_2 = Review.objects.create(email='sqwrqwr@gmail.com', name='Zeka',
                                         text ='My favorite product!',
                                         parent='Zeka',
                                         review_on_store='Bershka',product='Hoodie',)
        data = ReviewSerializer([review_1, review_2], many=True)
        expected_data = [
            {
                'email': review_1.email,
                'name': review_1.name,
                'text': review_1.text,
                'parent': review_1.parent,
                'review_on_store': review_1.review_on_store,
                'product': review_1.product
                    },

            {
                'email': review_2.email,
                'name': review_2.name,
                'text': review_2.text,
                'parent': review_2.parent,
                'review_on_store': review_2.review_on_store,
                'product': review_2.product

            },
        ]
        self.assertEqual(expected_data, data)
