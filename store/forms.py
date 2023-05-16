from django import forms
from django.forms import ModelForm
from .models import  Order





class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'email', 'city',) 


