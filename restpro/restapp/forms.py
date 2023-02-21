from django.contrib.auth.forms import UserCreationForm
from .models import Order
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class OrderFilter():
    pass
