from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('family', views.family, name='family'),
    path('profile', views.profile, name='profile')
]
