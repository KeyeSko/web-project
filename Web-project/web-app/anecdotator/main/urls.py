from django.urls import path, include
from . import views
from .views import Register, like_unlike_post

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('family/', views.family, name='family'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include("django.contrib.auth.urls")),
    #path('test/', views.anecdot_list_view, name='main-post-view'),
    path('register/', Register.as_view(), name='register'),
    path('family/liked/', like_unlike_post, name='like-post-view'),
]
