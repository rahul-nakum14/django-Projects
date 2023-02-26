from django.urls import path
from . import views
from main.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',home,name='home'),
    # path('edit-profile/<int:user_id>/', views.edit_profile, name='edit-profile'),
    path('edit-profile/',views.profile,name='lop'),


]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)