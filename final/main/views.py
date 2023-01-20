from django.shortcuts import render
from . forms import helomodel

def register(response):
    if response.method == 'POST':
        form = helomodel(response.POST)
        if form.is_valid():
            form.save()
    else:
            form = helomodel()
    return render(response,'main/register.html',{'form':form})