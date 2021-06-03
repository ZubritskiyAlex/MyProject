from django.contrib import admin
from .models import User, Store, Category, Product

admin.site.register(User)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Product)
