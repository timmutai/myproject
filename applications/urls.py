from django.urls import path
from . import views

urlpatterns = [
    
    path('applicationApproval/<int:pk>', views.applicationApproval.as_view(), name='applicationApproval'),
    path('applicationView', views.applicationView.as_view(), name='applicationView'),
    
    
    
    
]