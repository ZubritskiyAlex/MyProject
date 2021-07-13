from django.db.models import Count
from django.views import View

from teespring.models import User, Cart, Category

menu = ["Create product", "Create store", "Feedback", "About app"]



class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = User.objects.filter(user=request.user).first()
            if not customer:
                customer = User.objects.create(
                    user=request.user
                )
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)



class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('product'))
        user_menu = menu.copy
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
