from django import forms

class registrationform(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput())
    address = forms.CharField(widget=forms.Textarea())
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)