from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from .models import User, Store, Category, Product, Review, UsersProductsRelation, UsersStoresRelation, CartProduct, \
    Cart, Order, Customer, OrderItem, ShippingAddress


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Review"""
    list_display = ("name", "email", "parent", "product", "id")
    readonly_fields = ("name", "email")


class ReviewInline(admin.TabularInline):
    """Feedback on product's page"""
    model = Review
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Categories"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Products"""
    list_display = ("title", "category", "url", "draft", "get_image")
    readonly_fields = ("get_image",)
    list_filter = ("category", "price", 'stores')
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    fieldsets = (
        ('Price', {
            "classes": ("collapse",),
            "fields": (("title", "price"),)
        }),
        ('Product_information', {
            "classes": ("collapse",),
            "fields": ("description", "image", "get_image",)
        }),
        ('Stores_and_category', {
            "classes": ("collapse",),
            "fields": (("stores", "category", "is_tranding_category"),)
        }),

        ("Options", {
            "classes": ("collapse",),
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height = "110"')

    get_image.short_description = "Image"



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =("username", "email","is_owner","is_staff")
    list_editable = ("is_owner","is_staff")




@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "url", "description", "popular_product",)
    readonly_fields = ("get_image",)
    list_filter = ("date_created", "url", 'tranding_category')
    search_fields = ("name", "url", "popular_product")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    fieldsets = (
        ('Description', {
            "classes": ("collapse",),
            "fields": (("name", "description", "image"),)
        }),
        ('Popular', {
            "classes": ("collapse",),
            "fields": ("tranding_category", "popular_product",)
        }),

        ("Options", {
            "classes": ("collapse",),
            "fields": (("url",))
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height = "110"')

    get_image.short_description = "Image"


@admin.register(UsersProductsRelation)
class UsersProductsRelation(ModelAdmin):
    pass


@admin.register(UsersStoresRelation)
class UsersStoresRelation(ModelAdmin):
    pass

@admin.register(CartProduct)
class CartProduct(ModelAdmin):
    pass

@admin.register(Cart)
class Cart(ModelAdmin):
    pass


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
