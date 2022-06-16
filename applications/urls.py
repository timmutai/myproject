from django.urls import path
from . import views

urlpatterns = [
    
    path('applicationApproval/<int:pk>', views.applicationApproval.as_view(), name='applicationApproval'),
    path('applicationsView', views.applicationsView.as_view(), name='applicationsView'),
    
    
    
    
]