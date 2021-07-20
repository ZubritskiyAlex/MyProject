from django.db import models

from teespring.models import Product


class Reservation(models.Model):
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='name', max_length=50)
    phone = models.DateTimeField(verbose_name='phone', max_length=50)
    email = models.EmailField(verbose_name='email')
