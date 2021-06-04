from django.db import models, transaction
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
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
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="Description", blank=True, null=True)
    image = models.ImageField(verbose_name='Photo')
    date_created = models.DateField(auto_now=True)


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

    def __str__(self):
        return f"{self.user} - {self.name}-{self.description}-{self.url}"

    class Meta:

        db_table = _("Store")
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Name of category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:

        db_table = _("Category")
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


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

        db_table = _("Product")
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
