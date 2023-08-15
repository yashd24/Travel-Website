from .models import places
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MyForm(ModelForm):
    class Meta:
        model = places
        fields = '__all__'


class signup_form(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
