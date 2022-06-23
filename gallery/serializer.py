from rest_framework import serializers
from .models import Gallery, album


class albumSerializer(serializers.ModelSerializer):       
    
    class Meta:
        model= album
        fields='__all__'

class GallerySerializer(serializers.ModelSerializer):       
    
    class Meta:
        model= Gallery
        fields='__all__'


        