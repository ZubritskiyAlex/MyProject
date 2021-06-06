from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Store, Category, Product, Review


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
    list_filter = ("category", "price", 'date_created', 'stores')
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
            "fields": ("description", "image", "get_image", "date_created")
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


#@admin.register(ProductShots)
#class ProductShotsInLine(admin.TabularInline):
#    model = ProductShots
#    extra = 1
#    readonly_fields = ("get_image",)

#    def get_image(self, obj):
#        return mark_safe(f'<img src={obj.image.url} width="100" height = "110"')

    #get_image.short_description = "Image"


admin.site.register(User)
admin.site.register(Store)


