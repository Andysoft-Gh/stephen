from typing import OrderedDict
from .models import Order, Customer, Product
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model =Order
        fields ='__all__'
class CustomerForm(ModelForm):
    
    class Meta:
        model =Customer
        fields ='__all__'
