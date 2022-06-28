from unicodedata import category
from urllib import response
from .models import Gallery, album
from applications.pagination import ListViewPagination
from .serializer import GallerySerializer, albumSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters  import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from gallery import serializer


# Create your views here.



class albumView(generics.ListCreateAPIView):
    
    authentication_classes=[TokenAuthentication, SessionAuthentication]
    permission_classes=     [IsAuthenticated]

    queryset=album.objects.all()
    serializer_class=albumSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_student:
            category=self.get_queryset()
            if category:
                serializer=self.get_serializer(category, many=True)

                return Response(serializer.data)
            else: 
                return Response({'response':'No photo albums to display'})

        else:
            return Response('Access Denied: only students can view this page')

    def create(self, request, *args, **kwargs):
        if request.user.is_student:
            serializer=self.get_serializer(data=request.data)
            user=self.request.user
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response('only students can create  albums')
class galleyView(generics.ListCreateAPIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=     [IsAuthenticated]
    pagination_class=ListViewPagination
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    filterset_fields = ['id', 'album']
    search_fields = ['caption',]


    queryset=Gallery.objects.all()
    serializer_class=GallerySerializer

    def list(self, request, *args, **kwargs):
        photos=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(photos, many=True)
        if request.user.is_student:
            if photos:
                return Response(serializer.data)
            else:
                return Response({'response': 'No photos to display'})
        else:
            return Response({'response':'Access Denied: only students can view this page'})

    def create(self, request, *args, **kwargs):
        if request.user.is_student:
            
            serializer=self.get_serializer(data=request.data)
            user=self.request.user
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({'response':'only students can upload photos'})

   
