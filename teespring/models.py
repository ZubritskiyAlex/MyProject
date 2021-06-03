from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


TRENDING_CATEGORIES = (
    (1, 'Digital',),
    (2, 'Apparel',),
    (3, 'Accessories',),
    (4, 'Premium AS Colour Collection',),
    (5, 'Conscious Collection',),
    (6, 'Home',),
)

TRENDING_PRODUCTS = (
    (1,'Staple Tee',),
    (2,'Premium Hoodie',),
    (3, 'Face Masks',),

)


class User(models.Model):

    name = models.CharField(max_length=100, verbose_name="Your name or Brand name")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email")
    password = models.CharField(max_length=30, verbose_name="Password")
    image = models.ImageField(verbose_name='Image')
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(102)],
        verbose_name="Age",
        default=0
    )

    date_created = models.DateField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:

        db_table = "User"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Store(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Store name")
    url = models.URLField(verbose_name='URL', blank=True, null=True, unique=True)
    description = models.TextField("Description")
    tranding_category = models.IntegerField(choices=TRENDING_CATEGORIES)
    popular_product = models.IntegerField(choices=TRENDING_PRODUCTS)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.name}-{self.description}-{self.url}"

    class Meta:

        db_table = "Store"
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:

        db_table = "Category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):

    title = models.CharField(max_length=255, verbose_name="Product name")
    stores = models.ManyToManyField(Store, verbose_name='Stores')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Price", default=0)
    date_created = models.DateField(auto_now=True)
    is_tranding_category = models.BooleanField(default=False)
    image = models.ImageField(verbose_name='Image')


    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:

        db_table = "Product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
