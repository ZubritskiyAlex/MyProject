from django import forms
from django.forms import ModelForm

from .models import Review, Product, Store, Order


class AddReviewForm(forms.ModelForm):
    """Form review"""

    class Meta:
        model = Review
        fields = '__all__'

    def save(self, **kwargs):
        review = Review(**self.cleaned_data)
        review.save()
        return review


class AddProductForm(forms.ModelForm):
    """Add product form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category not selected"

    class Meta:
        model = Product
        fields = ['title', 'stores', 'description', 'price', 'image', 'url']

    def save(self, **kwargs):
        product = Product(**self.cleaned_data)
        product.save()
        return product


class AddStoreForm(forms.ModelForm):
    """Add store form"""

    class Meta:
        model = Store
        fields = ['name', 'url', 'description', 'tranding_category']

    def save(self, **kwargs):
        store = Store(**self.cleaned_data)
        store.save()
        return store


class OrderForm(ModelForm):
    """Add order form"""

    class Meta:
        model = Order
        fields= '__all__'

    def save(self, **kwargs):
        order = Order(**self.cleaned_data)
        order.save()
        return order
