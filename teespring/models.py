from django.db import models, transaction
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)



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

class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
            return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, blank=True)
    email = models.EmailField(max_length=40, unique=True)
    is_staff = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="Description", blank=True, null=True)
    image = models.ImageField(verbose_name='Photo',null=True)
    date_created = models.DateField(auto_now=True)
    is_owner = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        db_table = _('User')
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Store(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Store name")
    url = models.URLField(verbose_name='URL', blank=True, null=True, unique=True)
    description = models.TextField("Description")
    tranding_category = models.IntegerField(choices=TRENDING_CATEGORIES)
    popular_product = models.IntegerField(choices=TRENDING_PRODUCTS)
    date_created = models.DateField(auto_now=True)
    image = models.ImageField(verbose_name='Image', null=True)
    category = models.ForeignKey('Category', verbose_name='Category', on_delete=models.PROTECT,null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null=True, related_name='my_stores')
    customers = models.ManyToManyField(User, through="UsersStoresRelation",
                                  null=True, related_name='stores')

    def __str__(self):
        return f"{self.user} - {self.name}-{self.description}-{self.url}"

    def get_absolute_url(self):
        return reverse('store', kwargs={'store_id': self.pk})

    class Meta:
        db_table = _("Store")
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Name of category')
    slug = models.SlugField(unique=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


    class Meta:

        db_table = _("Category")
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):

    title = models.CharField(max_length=255, verbose_name="Product name")
    stores = models.ManyToManyField(Store, verbose_name='Stores')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT, null=True)
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Price", default=0)
    date_created = models.DateField(auto_now=True)
    is_tranding_category = models.BooleanField(default=False)
    image = models.ImageField(verbose_name='Image',null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True, unique=True)
    draft = models.BooleanField("Draft", default=False)

    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='my_products')
    customers = models.ManyToManyField(User, through="UsersProductsRelation", related_name='products')


    def __str__(self):
        return f"{self.title} - {self.price}"

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:

        db_table = _("Product")
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Review(models.Model):
    """Reviews"""
    email = models.EmailField(verbose_name="Email")
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    review_on_store = models.ForeignKey(Store, verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class UsersProductsRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices= RATE_CHOICES,null=True)
    date_created = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} - {self.product.title}, RATE {self.rate}"


class UsersStoresRelation(models.Model):

    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    date_created = models.DateField()



    def __str__(self):
        return f"{self.user.username} - {self.store.description}, RATE {self.rate}"


class CartProduct(models.Model):

    user = models.ForeignKey(User, verbose_name='Buyer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    qty = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total_price')

    def __str__(self):
        return "Product: {} (for cartproduct)".format(self.product.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):

    owner = models.ForeignKey(User, null=True, verbose_name='Owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Total_price')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.id:
            self.total_products = self.products.count()
            self.final_price = sum([cproduct.final_price for cproduct in self.products.all()])
        super().save(*args, **kwargs)


class Order(models.Model):

    STATUS_NEW = 'New'
    STATUS_IN_PROGRESS = 'In_progress'
    STATUS_READY = 'Is_ready'
    STATUS_COMPLETED = 'Completed'

    BUYING_TYPE_SELF = 'Self delivery'
    BUYING_TYPE_DELIVERY = 'Delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'New order'),
        (STATUS_IN_PROGRESS, 'The order is being processed'),
        (STATUS_READY, 'Order is ready'),
        (STATUS_COMPLETED, 'The order is completed')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Delivery self'),
        (BUYING_TYPE_DELIVERY, 'Delivery')
    )

    buyer = models.ForeignKey(User, verbose_name='Buyer', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Name')
    last_name = models.CharField(max_length=255, verbose_name='Last_name')
    phone = models.CharField(max_length=20, verbose_name='Phone number')
    cart = models.ForeignKey(Cart, verbose_name='Cart', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='adress', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Status order',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Type order',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Comment to order', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Date created order')
    order_date = models.DateField(verbose_name='Date delivery order', default=timezone.now)

    def __str__(self):
        return str(self.id)
