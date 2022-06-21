from .models import Gallery
from .serializer import GallerySerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters  import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class photos(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=     [IsAuthenticated]

    queryset=Gallery.objects.all()
    serializer_class=GallerySerializer

    def list(self, request, *args, **kwargs):
        # if request.user.is_student:
        return super().list(request, *args, **kwargs)

        # else:
        #     return Response('Access Denied: only students can view this page')

    def create(self, request, *args, **kwargs):
        if request.user.is_student:
            return super().create(request, *args, **kwargs)
        else:
            return Response('only students can upload photos')

   