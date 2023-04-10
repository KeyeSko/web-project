from django.urls import path
from . import views
from .views import RegisterUser

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('family', views.family, name='family'),
    path('profile', views.profile, name='profile'),
    path('register', RegisterUser.as_view(), name='register')
]
