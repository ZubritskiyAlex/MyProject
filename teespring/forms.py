from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Review, Product, Store, Order, User
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class AddReviewForm(forms.ModelForm):
    """Form review"""

    def __init__(self,*args,**kwargs):
        super(AddReviewForm, self).__init__(*args,**kwargs)
        self.fields['review_on_store'].empty_label = "Store not selected"


    class Meta:
        model = Review
        fields = '__all__'

    def save(self, **kwargs):
        review = Review(**self.cleaned_data)
        review.save()
        return review


class AddProductForm(forms.ModelForm):
    """Add product form"""
    def __init__(self,*args,**kwargs):
        super(AddProductForm, self).__init__(*args,**kwargs)
        self.fields['category'].empty_label = "Category not selected"
        

    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('The length exceeds 200 characters')

        return title


class AddStoreForm(forms.ModelForm):
    """Add store form"""

    def __init__(self,*args,**kwargs):
        super(AddStoreForm, self).__init__(*args,**kwargs)
        self.fields['category'].empty_label = "Category not selected"

    class Meta:
        model = Store
        fields = '__all__'


    def save(self, **kwargs):
        store = Store(**self.cleaned_data)
        store.save()
        return store


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('The length exceeds 200 characters')

        return title


class OrderForm(ModelForm):
    """Add order form"""

    class Meta:
        model = Order
        fields= '__all__'

    def save(self, **kwargs):
        order = Order(**self.cleaned_data)
        order.save()
        return order



class LoginUserForm(AuthenticationForm):
    """Login User form"""
    username = forms.CharField(label='Log in', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login'
        self.fields['password'].label = 'Password'


    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'User with login {username} not found')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Wrong password!')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username','password']


class RegisterUserForm(UserCreationForm):
    """Register form"""

    username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class':'form-input'}))
    first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={'class':'form-input'}))
    last_name = forms.CharField(label='Last name',widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','image','email','is_owner')
