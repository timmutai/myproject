from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('UserCreation', views.UserCreation.as_view(), name='index'),
    path('login', auth_view.obtain_auth_token),
    
]