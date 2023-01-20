from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class helomodel(UserCreationForm):
    email = forms.EmailField()
    class meta:
        fields = ['username','email','password1','password2']