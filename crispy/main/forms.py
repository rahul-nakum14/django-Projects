from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import post_model,Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}))
    email = forms.EmailField(max_length=20, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
  
class UserUpdadeform(forms.ModelForm):
    email =  forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
 
class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image']
       

class post_form(forms.ModelForm):
    class Meta:
        model = post_model
        fields = ['title','description','is_private']

        # widgets ={
        #     'title': forms.TextInput(attrs={'class': 'form-control'})
        # }


    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'