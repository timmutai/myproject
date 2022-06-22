from users.models import users
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from cryptography.fernet import Fernet

class UserCreationSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(UserCreationSerializer, self).__init__(*args, **kwargs)
        self.fields['phone_No'].label = 'Phone No (Example: +254700000000)'    
        
    
    class Meta:
        model= users
        fields=['firstName','lastName','idno','phone_No','address','country','email','is_student','is_sponsor','password']
        extra_kwargs={'password':{'write_only':True}}
       
        def create(self, validated_data):
            user = users(
                email=validated_data['email'],

                
            )
            
            user.set_password('password')
            user.save()
            return user