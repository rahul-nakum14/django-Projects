from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    return render(requests,'app1/home.html')
def login(requests):
    return render(requests,'app1/login.html')

def signup(requests):
    return render(requests,'app1/signup.html')

    # context = dict(post)
    # return render(requests,'app1/home.html',context)


    # context = {
    #     'posts':post
    # }
    # return render(requests,'app1/home.html',context)
    

    