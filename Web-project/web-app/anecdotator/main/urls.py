from django.urls import path, include
import django.contrib.auth.urls
from . import views
from .views import Register, like_unlike_post

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('family/', views.AnecListView.as_view(), name='family'),
    path('profile', views.profile, name='profile'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('test/', views.post_comment_create_and_list_view, name='main-post-view'),
    path('register/', Register.as_view(), name='register'),
    path('test/liked/', like_unlike_post, name='like-post-view'),
]
