from django.urls import path, include
import django.contrib.auth.urls
from . import views
from .views import Register


urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('family', views.family, name='family'),
    path('profile', views.profile, name='profile'),
    path('accounts/', include("django.contrib.auth.urls")),
    #path('accounts', views.profile, name='profile'),
    path('register', Register.as_view(), name='register')
    #path('', include(('home.urls', 'home'), namespace='home'))
]
