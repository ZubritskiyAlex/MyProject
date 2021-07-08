from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Review, Product, Store, Order, User, Category


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



class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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


class RegistrationForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password =forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Login'
        self.fields['password'].label = 'Password'
        self.fields['confirm_password'].label = 'Confirm_password'
        self.fields['phone'].label = 'Phone number'
        self.fields['first_name'].label = 'Your first name'
        self.fields['address'].label = 'Adress'
        self.fields['email'].label = 'Email'

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['com', 'net']:
            raise forms.ValidationError(f'Registration for domain {domain} impossible')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address has already been registered')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Name {username} occupied')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('passwords dont match')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name','phone', 'email']
