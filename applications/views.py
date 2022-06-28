from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters  import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from yaml import serialize
from .serializers import applicationSerializer
from .models import applications
from django.core.mail import send_mail


# Apiview to handle cration of application by students and staff/sponsors can  retrieve/search list of applications

class applicationView(generics.ListCreateAPIView):
                 
    queryset=applications.objects.all()
    serializer_class=applicationSerializer
    authentication_classes= [TokenAuthentication,]
    permission_classes=[IsAuthenticated,] 
    pagination_class=PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    filterset_fields = ['id', 'school_name']
    search_fields = ['school_name']

    
    
    def create(self, request, *args, **kwargs):
        if request.user.is_student:
            
            serializer = self.get_serializer(data=request.data)
            user=self.request.user

            if serializer.is_valid():
                
                serializer.save(user=user)
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({'response':'You dont have permission to create an application, only students can create applications'})
    
   
    def list(self, request, *args, **kwargs):
        
        if request.user.is_sponsor:
            approved=self.filter_queryset(self.get_queryset().filter(staffapproval=True))
            serailazer=self.get_serializer(approved, many=True)
            
            if approved:
                return Response(data=serailazer.data)
            else:
                return Response({'response':'No approved applications to display'}) 

        elif request.user.is_staff:
            response= self.filter_queryset(self.get_queryset())
            serailazer=self.get_serializer(response, many=True)
            if response:
                return Response(serailazer.data)    
            else:
                return Response({'response':'No applications to display'})    
        else:
            return Response({'response':'You dont have permission to view list of applications'})

class applicationApproval(generics.RetrieveUpdateAPIView):

    authentication_classes= [TokenAuthentication]
    permission_classes=[IsAuthenticated]

    queryset=applications.objects.filter()
    serializer_class=applicationSerializer 
    lookup_field = 'pk'
            
    def retrieve(self, request, pk,*args, **kwargs):
        
        
        if request.user.is_staff:
               
            application=self.get_queryset().filter(pk=pk)
            if application:
                serailazer=self.get_serializer(application,many=True)
                return Response(serailazer.data)
            else:
                return Response ({'response': 'No records to display'})
            
        if request.user.is_sponsor:
            approved=self.get_queryset().filter(staffapproval=True,id=pk)

            if approved:
                serailazer=self.get_serializer(approved, many=True)            
                return Response(data=serailazer.data)
            else:
                return Response ({'response': 'This application have not been approved by the staff'})
           

        else:
            return Response({'response':'Access Denied: you dont have permission to view this resource'})

    
    def update(self, request,  *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if serializer.is_valid():

            if self.request.user.is_student:
                return Response({'response':'Access Denied: your dont have permission to view this page'})

            if self.request.user.is_staff:
                
                serializer.save()

                emails=applications.objects.filter().first()
                mail=emails.user.email                            
    
                try:
                
                    send_mail(
                        'Spornsorship', # subject
                        'Your application for sponsorship has been approved by a staff, Kindly wait for sponsorship',  # message
                        '', # sender
                        [mail], #receiver
                        fail_silently=False,
    
                    )    
                
                except:
                    return Response({'response':'An error occured while sending email, please try again'})    
                return Response(request.data)            
                          
            if self.request.user.is_sponsor and instance.staffapproval:
                serializer.save()

                emails=applications.objects.filter().first()
                mail=emails.user.email 
           
                if serializer.save():
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
                    
                    except:
                        return Response({'response':'An error occured while sending email, please try again'})
                return Response(request.data)

            else:
                return Response({'response':'The application have not been approved by the staff'})

        


        return Response(serializer.errors)