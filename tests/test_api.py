import json

from django.db.models import When, Case, Count, Avg
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from api.serializers import ProductSerializer, StoreSerializer, UserSerializer, CategorySerializer, ReviewSerializer
from teespring.models import Product, Store, User, Review, Category, UsersProductsRelation, UsersStoresRelation


class ProductApiTestCase(APITestCase):

    def SetUp(self):
        self.user = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                     first_name="Alexander", last_name="Zubritskiy",

                                     url="https://dagadf.com", description="asafasfc", image=None,

                                     date_created="26.04.2000", is_owner=False,
                                     )

        self.product_1 = Product.objects.create(title="Phone", stores="TechnoStore", category="Digital", description="Devices Store",
                                           price="500.00", date_created="01.09.2003", is_tranding_category=True,
                                           image=None, url="https://mi-shop.by/", draft=True, owner=self.user
                                           )
        self.product_2 = Product.objects.create(title="Hoodie", stores="Bershka", category="clothes", description="test_2",
                                           price="255.00", date_created="11.11.2000", is_tranding_category=True,
                                           image=None, url="https://www.bershka.com/", draft=False, owner="Petr"
                                           )
        self.product_3 = Product.objects.create(title="test3", stores="Bershka", category="clothes", description="Сlothes configureStore",
                                           price="250.00", date_created="11.07.2005", is_tranding_category=True,
                                           image=None, url="https://www.bershka.com/", draft=False, owner="Zeka"
                                           )

    def test_get(self):
        url = reverse('product-list')
        response = self.client.get(url)
        products = Product.objects.all().annotate(

        )

        serializer_data = ProductSerializer(products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)




    def test_get_search(self):
        url = reverse('product-list')
        response = self.client.get(url,data={'search': 'Test_product_1'})
        serializer_data = ProductSerializer([self.product_1, self.product_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_create(self):
        self.assertEqual(3, Product.objects.all().count())
        url = reverse('product-list')
        data = {
            'title': "Phone",
            'shops': "TechnoStore",
            'category': "Digital",
            'description': "Devices Store",
            'price': "500.00",
            'date_created': "01.09.2003",
            'is_tranding_category': True,
            'image': None,
            'url': "https://mi-shop.by/",
            'draft': False,
            'owner': "Alex",
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Product.objects.all().count())


    def test_update(self):

        url = reverse('product-detail', args=(self.product_1.id))
        data = {
            'title': self.product_1.title,
            'shops': self.product_1.stores,
            'category': self.product_1.category,
            'description': self.product_1.description,
            'price': 480,
            'date_created': "01.09.2003",
            'is_tranding_category': self.product_1.is_tranding_category,
            'image':self.product_1.image,
            'url': self.product_1.url,
            'draft': self.product_1.draft,
            'owner': self.product_1.owner,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.product_1.refresh_from_db()
        self.assertEqual(480, self.product_1.price)


    def test_update_not_owner(self):
        self.user2 = User.objects.create(username='test_user2',)
        url = reverse('product-detail', args=(self.product_1.id,))
        data = {
            'title': self.product_1.title,
            'shops': self.product_1.stores,
            'category': self.product_1.category,
            'description': self.product_1.description,
            'price': 410,
            'date_created': "01.09.2003",
            'is_tranding_category': self.product_1.is_tranding_category,
            'image':self.product_1.image,
            'url': self.product_1.url,
            'draft': self.product_1.draft,
            'owner': self.product_1.owner,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user2)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.product_1.refresh_from_db()
        self.assertEqual(500, self.product_1.price)



    def test_update_not_owner_but_staff(self):
        self.user2 = User.objects.create(username='test_user2', is_staff=True)
        url = reverse('product-detail', args=(self.product_1.id,))
        data = {
            'title': self.product_1.title,
            'shops': self.product_1.stores,
            'category': self.product_1.category,
            'description': self.product_1.description,
            'price': 410,
            'date_created': "01.09.2003",
            'is_tranding_category': self.product_1.is_tranding_category,
            'image':self.product_1.image,
            'url': self.product_1.url,
            'draft': self.product_1.draft,
            'owner': self.product_1.owner,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user2)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.product_1.refresh_from_db()
        self.assertEqual(410, self.product_1.price)


class StoreApiTestCase(APITestCase):

    def SetUp(self):
        self.user = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                        first_name="Alexander", last_name="Zubritskiy",

                                        url="https://dagadf.com", description="asafasfc", image=None,

                                        date_created="26.04.2000", is_owner=False,
                                        )

        self.store_1 = Store.objects.create(user="Alex", name="TecStore", url="https://dagzdaxaqwdaf.com",

                                       description ="Devices shop",

                                       tranding_category="Clothes",popular_product='Face mask',

                                       date_created="27.02.1990", image=None,

                                     )

        self.store_2 = Store.objects.create(user= "Zeka", name="TechnoStore", url="https://dagzdaqwdaf.com",

                                       description ="Devices shop",

                                       tranding_category="Clothes",popular_product='Face mask',

                                       date_created="27.02.1990", image=None,

                                       )
        self.store_3 = Store.objects.create(user="Zeka", name="test_store", url="https://dagzdaqwdaf.com",

                                       description="Test_3",

                                       tranding_category="Clothes", popular_product='Face mask',

                                       date_created="27.02.1990", image=None,

                                       )

    def test_get(self):
        url = reverse('configureStore-list')
        response = self.client.get(url)
        stores = Store.objects.all().annotate(
            id__in=[self.store_1.id, self.store_2.id, self.store_3.id]).annotate(
            annotated_likes=Count(Case(When(usersstoresrelation__like=True, then=1))),rating=Avg('usersstoresrelation__rate').order_by('id'))
        serializer_data = StoreSerializer(stores,many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)




    def test_get_search(self):
        url = reverse('configureStore-list')
        response = self.client.get(url, data={'search': 'Test_product_1'})
        serializer_data = StoreSerializer([self.store_1, self.store_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_create(self):
        self.assertEqual(3, Store.objects.all().count())
        url = reverse('configureStore-list')
        data = {
            "user": "Alex",
            "name": "TecStore",
            "url": "https://dagzdaxaqwdaf.com",
            "description": "Devices shop",
            "image": None,
            "date_created": "27.02.1990",
            "tranding_category" : "Clothes",
            "popular_product": 'Face mask',
        }

        json_data = json.dumps(data)

        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Store.objects.all().count())


    def test_update(self):
        url = reverse('configureStore-detail', args=(self.store_1.id))
        data = {
            "user": self.store_1.user,
            "name": "Device shop",
            "url": self.store_1.url,
            "description": self.store_1.description,
            "image":self.store_1.image,
            "date_created": self.store_1.date_created,
            "tranding_category": self.store_1.tranding_category,
            "popular_product": self.store_1.popular_product,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.store_1.refresh_from_db()
        self.assertEqual("Device shop", self.store_1.name)


    def test_update_not_owner(self):
        self.user2 = User.objects.create(username='test_user2',)
        url = reverse('configureStore-detail', args=(self.store_1.id,))
        data = {

            "user": self.store_1.user,
            "name": "Device shop",
            "url": self.store_1.url,
            "description": self.store_1.description,
            "image": self.store_1.image,
            "date_created": self.store_1.date_created,
            "tranding_category": self.store_1.tranding_category,
            "popular_product": self.store_1.popular_product,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user2)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual({'detail':ErrorDetail(string='You do not have permission to perform this actions.', code='permission_denied')},
                         response.data)
        self.store_1.refresh_from_db()
        self.assertEqual('TecStore', self.store_1.name)


    def test_update_not_owner_but_staff(self):
        self.user2 = User.objects.create(username='test_user2',is_staff=True)
        url = reverse('configureStore-detail', args=(self.store_1.id,))
        data = {

            "user": self.store_1.user,
            "name": "Device shop",
            "url": self.store_1.url,
            "description": self.store_1.description,
            "image": self.store_1.image,
            "date_created": self.store_1.date_created,
            "tranding_category": self.store_1.tranding_category,
            "popular_product": self.store_1.popular_product,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user2)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.store_1.refresh_from_db()
        self.assertEqual("Device shop", self.store_1.name)



class UserApiTestCase(APITestCase):

    def SetUp(self):
        self.user = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                        first_name="Alexander", last_name="Zubritskiy",

                                        url="https://dagadf.com", description="asafasfc", image=None,

                                        date_created="26.04.2000", is_owner=False,
                                        )
        self.user_1 = User.objects.create(username ="Alex",email ="abc@gmail.com",is_staff =False,

                                     first_name = "Alexander",

                                     last_name="Zubritskiy",url ="https://dagadf.com",description ="asafasfc",image =None,

                                     date_created="26.04.2000",is_owner =False,

                                     )
        self.user_2 = User.objects.create(username ="Zekych",email ="axvabc@gmail.com",is_staff =False,
                                     first_name = "Zeka",
                                     last_name="Zekov",url ="https://dagzdafadf.com",description ="axzvvsafasfc",image =None,
                                     date_created="27.02.2005",is_owner =False,
                                     )
        self.user_3 = User.objects.create(user= "Dima", name="test_store_3", url="https://dagzdaqwdaf.com",
                                       description ="test_shop_3",
                                       tranding_category="Clothes",popular_product='Face mask',
                                       date_created="27.05.1997", image=None,
                                       )

    def test_get(self):
        url = reverse('user-list')
        response = self.client.get(url)
        serializer_data = UserSerializer.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('user-list')
        response = self.client.get(url, data={'search': 'Test_product_1'})
        serializer_data = UserSerializer([self.user_1, self.user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_user(self):
        self.assertEqual(3, User.objects.all().count())
        url = reverse('user-list')
        data = {
                "username": "Alex",
                "email" :"abc@gmail.com",
                "is_staff" : False,
                "first_name" : "Alexander",
                "last_name": "Zubritskiy",
                "url" : "https://dagadf.com",
                "description" : "asafasfc",
                "image" : None,
                "date_created" :"26.04.2000",
                "is_owner": False,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                        content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, User.objects.all().count())


    def test_update_user(self):
        url = reverse('user-detail', args=(self.user_1.id))
        data = {
            "username": "Petr",
            "email": self.user_1.email,
            "is_staff": self.user_1.is_staff,
            "first_name": self.user_1.first_name,
            "last_name": self.user_1.last_name,
            "url": self.user_1.url,
            "description": self.user_1.description,
            "image": self.user_1.image,
            "date_created": self.user_1.date_created,
            "is_owner": self.user_1.is_owner,


            }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                       content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.user_1.refresh_from_db()
        self.assertEqual("Petr", self.user_1.username)



class ReviewApiTestCase(APITestCase):
    def SetUp(self):
        self.user = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                        first_name="Alexander", last_name="Zubritskiy",

                                        url="https://dagadf.com", description="asafasfc", image=None,

                                        date_created="26.04.2000", is_owner=False,
                                        )
        self.review_1 = Review.objects.create(email ='sdgba@gmail.com',name ='Alex',
                                         text ='Best configureStore in the world!',
                                         parent ='Alex',
                                         review_on_store ='Techno',product='Phone',)

        self.review_2 = Review.objects.create(email='sqwrqwr@gmail.com', name='Zeka',
                                         text ='My favorite product!',
                                         parent='Zeka',
                                         review_on_store='Bershka_test',product='Hoodie',)

        self.review_3 = Review.objects.create(email='sqwrqwr@gmail.com', name='Zeka',
                                         text ='My favorite product!',
                                         parent='Dima',
                                         review_on_store='Bershka',product='Hoodie',)

    def test_get(self):
        url = reverse('review-list')
        response = self.client.get(url)
        serializer_data = ReviewSerializer.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('product-list')
        response = self.client.get(url,data={'search': 'Test_product_1'})
        serializer_data = ReviewSerializer([self.review_1, self.review_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Review.objects.all().count())
        url = reverse('configureStore-list')
        data = {
            "email": 'sdgba@gmail.com',
            "name":'Alex',
            "text": 'Best configureStore in the world!',
            "parent": 'Alex',
            "review_on_store": 'Techno',
            "product": 'Phone'
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Review.objects.all().count())


    def test_update(self):
        url = reverse('review-detail', args=(self.review_1.id))
        data = {
            "email": self.review_1.email,
            "name": self.review_1.name,
            "text": "Great!" ,
            "parent": self.review_1.parent ,
            "review_on_store": self.review_1.review_on_store,
            "product": self.review_1.product
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.review_1.refresh_from_db()
        self.assertEqual("Great!", self.review_1.text)


class CategoryApiTestCase(APITestCase):

    def SetUp(self):
        self.user = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                        first_name="Alexander", last_name="Zubritskiy",

                                        url="https://dagadf.com", description="asafasfc", image=None,

                                        date_created="26.04.2000", is_owner=False,
                                        )

        self.category_1 = Category.objects.create(name ="Digital",slug='digit',
                                                  url='https://dagzdaqasfwdaf.com',)

        self.category_2 = Category.objects.create(name ="Clothes",slug="wear", url='https://dqwfaxvf.com',)

        self.category_3 = Category.objects.create(name ="Home",slug="test_3", url='https://dqwfaxvf.com',)

    def test_get(self):
        url = reverse('category-list')
        response = self.client.get(url)
        serializer_data = CategorySerializer.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('category-list')
        response = self.client.get(url,data={'search': 'Test_product_1'})
        serializer_data = CategorySerializer([self.category_1, self.category_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_create(self):
        self.assertEqual(3, Category.objects.all().count())
        url = reverse('product-list')
        data = {
            "name": "Digital",
            "slug": 'digit',
            "url": 'https://dagzdaqasfwdaf.com'

        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Category.objects.all().count())


    def test_update(self):
        url = reverse('product-detail', args=(self.category_1.id))
        data = {
            "name": "Digital",
            "slug": 'Clothes',
            "url": 'https://dagzdaqasfwdaf.com'
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.category_1.refresh_from_db()
        self.assertEqual('Clothes', self.category_1.slug)


class UsersProductRelationTestCase(APITestCase):

    def SetUp(self):
        self.user = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                     first_name="Alexander", last_name="Zubritskiy",

                                     url="https://dagadf.com", description="asafasfc", image=None,

                                     date_created="26.04.2000", is_owner=False,
                                     )

        self.user_2 = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                        first_name="Zeka", last_name="Zekov",

                                        url="https://dagadf.com", description="asafasfc", image=None,

                                        date_created="26.04.2000", is_owner=False,
                                        )

        self.product_1 = Product.objects.create(title="Phone", stores="TechnoStore", category="Digital", description="Devices Store",
                                           price="500.00", date_created="01.09.2003", is_tranding_category=True,
                                           image=None, url="https://mi-shop.by/", draft=True, owner=self.user
                                           )
        self.product_2 = Product.objects.create(title="Hoodie", stores="Bershka", category="clothes", description="test_2",
                                           price="255.00", date_created="11.11.2000", is_tranding_category=True,
                                           image=None, url="https://www.bershka.com/", draft=False, owner="Petr"
                                           )


    def test_like(self):
        url = reverse('userproductrelation-detail', args=(self.product_1.id,))

        data = {
            "like": True,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data,
                                     content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UsersProductsRelation.objects.get(user=self.user,
                                                     book=self.product_1)

        self.assertTrue(relation.like)

        data = {
            "in_bookmarks": True,
        }
        json_data =json.dumps(data)
        response = UsersProductsRelation.objects.get(user=self.user,
                                                     book=self.product_1)
        self.assertTrue(relation.in_bookmarks)

    def test_rate(self):
        url = reverse('userproductrelation-detail', args=(self.product_1.id,))

        data = {
            "rate": 3,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data,
                                     content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UsersProductsRelation.objects.get(user=self.user,
                                                     book=self.product_1)
        self.assertEqual(3, relation.rate)


    def test_rate_wrong(self):
        url = reverse('userproductrelation-detail', args=(self.product_1.id,))

        data = {
            "rate": 9,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data,
                                     content_type='application/json')

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code, response.data)


class UsersStoresRelationTestCase(APITestCase):

    def SetUp(self):
        self.user = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                     first_name="Alexander", last_name="Zubritskiy",

                                     url="https://dagadf.com", description="asafasfc", image=None,

                                     date_created="26.04.2000", is_owner=False,
                                     )

        self.user_2 = User.objects.create(username="Alex", email="abc@gmail.com", is_staff=False,

                                        first_name="Zeka", last_name="Zekov",

                                        url="https://dagadf.com", description="asafasfc", image=None,

                                        date_created="26.04.2000", is_owner=False,
                                        )
        self.store_1 = Store.objects.create(user="Alex", name="TecStore", url="https://dagzdaxaqwdaf.com",

                                            description="Devices shop",

                                            tranding_category="Clothes", popular_product='Face mask',

                                            date_created="27.02.1990", image=None,

                                            )

        self.store_2 = Store.objects.create(user="Zeka", name="TechnoStore", url="https://dagzdaqwdaf.com",

                                            description="Devices shop",

                                            tranding_category="Clothes", popular_product='Face mask',

                                            date_created="27.02.1990", image=None,

                                            )

    def test_like(self):
        url = reverse('user_store_relation-detail', args=(self.store_1.id,))

        data = {
            "like": True,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data,
                                     content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UsersStoresRelation.objects.get(user=self.user,
                                                     book=self.store_1)

        self.assertTrue(relation.like)

        data = {
            "in_bookmarks": True,
        }
        json_data =json.dumps(data)
        response = UsersStoresRelation.objects.get(user=self.user,
                                                     book=self.store_1)
        self.assertTrue(relation.in_bookmarks)

    def test_rate(self):
        url = reverse('user_store_relation-detail', args=(self.store_1.id,))

        data = {
            "rate": 3,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data,
                                     content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UsersStoresRelation.objects.get(user=self.user,
                                                     store=self.store_1)
        self.assertEqual(3, relation.rate)


    def test_rate_wrong(self):
        url = reverse('userproductrelation-detail', args=(self.store_1.id,))

        data = {
            "rate": 9,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data,
                                     content_type='application/json')

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code, response.data)
