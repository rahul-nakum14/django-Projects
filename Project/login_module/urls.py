from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_page),
    path('login/', views.login_page,name="login"),
]
