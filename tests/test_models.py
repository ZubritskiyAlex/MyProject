from django.test import TestCase


from teespring.models import Product, Review, Category, Store, User


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title="Phone", stores="TechnoStore", category="Digital",
                               description="Devices Store", price="500.00",
                               date_created="01.09.2003", is_tranding_category=True,
                               image=None, url="https://mi-shop.by/", draft=False,)

    def test_title_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Product name')

    def test_stores_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('stores').verbose_name
        self.assertEquals(field_label,'Stores')

    def test_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEquals(field_label,'Category')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Description')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Price')

    def test_image_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Image')

    def test_url_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'URL')

    def test_title_max_length(self):
        title = Product.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_price_length(self):
        price = Product.objects.get(id=1)
        max_digits = price._meta.get_field('first_name').max_digits
        self.assertEquals(max_digits, 12)


class ReviewModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Review.objects.create(email='sqwrqwr@gmail.com', name='Zeka', text='My favorite product!',
        parent='Zeka', review_on_store='Bershka', product='Hoodie',)

    def test_email_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Email')

    def test_name_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_name_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


    def test_text_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Message')

    def test_text_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('text').max_length
        self.assertEquals(max_length, 5000)

    def test_parent_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('parent').verbose_name
        self.assertEquals(field_label, 'Parent')

    def test_review_on_store_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('review_on_store').verbose_name
        self.assertEquals(field_label, 'Parent')

    def test_product_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('product').verbose_name
        self.assertEquals(field_label, 'Product')


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="Clothes", slug="wear", url='https://dqwfaxvf.com', )

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_review_on_store_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'URL')


class StoreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Store.objects.create(user="Petr", name="TechnoStore", url="https://dagzdaqwdaf.com",
                        description="Devices shop", tranding_category="Digital",
                        popular_product='Staple Tee',
                        date_created="27.02.1993", image=None,)

    def test_name_label(self):
        store = Store.objects.get(id=1)
        field_label = store._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_name_max_length(self):
        store = Store.objects.get(id=1)
        max_length = store._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


    def test_image_label(self):
        store = Store.objects.get(id=1)
        field_label = store._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Image')

    def test_url_label(self):
        store = Store.objects.get(id=1)
        field_label = store._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'URL')


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username ="Alex",email ="abc@gmail.com",is_staff =False,
                                     first_name = "Alexander",
                                     last_name="Zubritskiy",url ="https://dagadf.com",description ="asafasfc",image =None,
                                     date_created="26.04.2000",is_owner =False,
                                     )

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max.length
        self.assertEquals(max_length, 30)

    def test_last_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max.length
        self.assertEquals(max_length, 30)

    def email_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max.length
        self.assertEquals(max_length, 40)

    def test_url_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'URL')

    def test_description_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Description')

    def test_description_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('description').max_length
        self.assertEquals(max_length, 255)

    def test_image(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Photo')
