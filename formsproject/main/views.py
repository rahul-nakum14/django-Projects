from django.shortcuts import render
from django.http import HttpResponse
from . forms import contactform,Snippetform

def contact(requests):
    if requests.method == 'POST':
        form = contactform(requests.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name,email)
    form = contactform(requests.POST)
    return render(requests,'main/create.html',{"form":form})


def snippet_details(requests):
    if requests.method == 'POST':
        form = Snippetform(requests.POST)

        if form.is_valid():
            form.save()
    form = Snippetform(requests.POST)
    return render(requests,'main/create.html',{"form":form})


# def create(requests):
#     form = list()
#     return render(requests,'main/create.html',{"form":form})

