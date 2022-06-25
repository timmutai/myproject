
from applications.models import applications
from rest_framework import serializers


class applicationSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=applications
        exclude=['user']


class studentSchoolSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(studentSchoolSerializer, self).__init__(*args, **kwargs)
        self.fields['year_of_completion'].label = 'Year of completion (yyyy-mm-dd)'
    class Meta:
        model=applications
        exclude=['sponsor','applicationDate','staffapproval','sponsorshipStatus']


class applicationApprovalSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=applications
        fields=['staffapproval']