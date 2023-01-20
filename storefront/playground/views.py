from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def helo_world(request):
#     return HttpResponse('helo world')

def helo_world(request):
    return render(request,'helo.html',{'name':'Rahul nakum'})

# def test():
#     x = 1
#     y = 2
#     return x+y











# def helo_world(request):
#     x = test()
#     return HttpResponse(str(x))



