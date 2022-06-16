from django.urls import path
from . import views

urlpatterns = [
    
    path('applicationApproval/<int:pk>', views.applicationApproval.as_view(), name='applicationApproval'),
    path('applicationsList', views.applicationsList.as_view(), name='applicationList'),
    # path('StudentSchoolInfo', views.StudentSchoolInfo.as_view(), name='StudentSchoolInfo'),
    
    
    
]