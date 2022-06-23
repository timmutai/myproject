from django.urls import path
from . import views

urlpatterns = [
    
    path('albumView', views.albumView.as_view(), name='albumView'),
    path('galleyView', views.galleyView.as_view(), name='galleyView'),      
    
]