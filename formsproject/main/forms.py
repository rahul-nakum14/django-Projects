from django import forms
from . models import Snippet


class contactform (forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="E-Mail")
    category = forms.ChoiceField(choices=[('questions','questions'),('other','other')])
    body = forms.CharField(widget=forms.Textarea)

class Snippetform(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name','body')