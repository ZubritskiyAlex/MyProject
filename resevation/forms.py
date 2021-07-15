from django import forms

from teespring.models import Product
from .models import Reservation


class ReservationForm(forms.ModelForm):
    product =forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Reservation
        fields = ['product', 'name','email', 'phone']