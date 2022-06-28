from rest_framework import serializers
from .models import Gallery, album


class albumSerializer(serializers.ModelSerializer):       
    
    class Meta:
        model= album
        exclude=['user']

class GallerySerializer(serializers.ModelSerializer):       
    
    class Meta:
        model= Gallery
        exclude=['user']


        