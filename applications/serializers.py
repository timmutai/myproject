
from applications.models import applications
from rest_framework import serializers


class applicationSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=applications
        exclude=['user','sponsorshipApproval','sponsor']





class applicationApprovalSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=applications
        fields=['staffapproval']