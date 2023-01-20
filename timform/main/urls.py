from django.contrib import admin
from django.urls import path
from . import views
from register import views as v


urlpatterns = [
    path('home',views.home,name="home"),
    path('register',v.register,name="register"),
]