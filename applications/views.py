from urllib import response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import applicationSerializer, studentSchoolSerializer
from rest_framework.filters  import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import applications
from django.core.mail import send_mail
from rest_framework import generics


# Apiview to handle cration of application by students and staff/sponsors can  retrieve/search list of applications

class applicationsView(generics.ListCreateAPIView):

    authentication_classes= [TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    queryset=applications.objects.all()
    serializer_class=applicationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'school_name']
    search_fields = ['school_name']

    
    
    def create(self, request, *args, **kwargs):
        if request.user.is_student:
            return super().create(request, *args, **kwargs)
        else:
            return Response('You dont have permission to create an application')
    
    def list(self, request, *args, **kwargs):

        

        if request.user.is_sponsor or request.user.is_staff:
            return super().list(request, *args, **kwargs)
        
        else:
            return Response('You dont have permission to create an application')
    

class applicationApproval(generics.RetrieveUpdateAPIView):

    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated]

    queryset=applications.objects.all()
    serializer_class=applicationSerializer 
    
    
    def retrieve(self, request, *args, **kwargs):
                
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):

        response= super().update(request, *args, **kwargs)
        emails=applications.objects.filter().first()
        mail=emails.idno.email
        if self.request.user.is_staff and response.status_code==200:                      
    
            try:
                
                send_mail(
                    'Spornsorship', # subject
                    'Your application for sponsorship has been approved by a staff, Kindly wait for sponsorship',  # message
                    '', # sender
                    [mail], #receiver
                    fail_silently=False,
    
                )    
                return Response(response)
            except:
                return Response('An error occured while sending email, please try again')    
                        
                          
        elif self.request.user.is_sponsor:
           
    
            try:
                emessage='Your application for sponsorship has been approved by a sponsor,Below are the sponsor details :'
                send_mail(
                        'Spornsorship', # subject
                        # message
                        f'{emessage},Name :{request.user.firstName},Email :{request.user.email},Phone :{request.user.phone_No},Country :{request.user.country}',
                        '', # sender
                        [mail], #receiver
                        fail_silently=False,
    
                )    
                return Response(response)
            except:
                return Response('An error occured while sending email, please try again')