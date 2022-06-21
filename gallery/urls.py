from django.urls import path
from . import views

urlpatterns = [
    
    path('photos', views.photos.as_view(), name='photos'),
    
    
    
    
    
]