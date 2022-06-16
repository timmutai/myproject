from users.models import users
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(UserCreationSerializer, self).__init__(*args, **kwargs)
        self.fields['phone_No'].label = 'Phone No (Example: +254700000000)'    
    
    
    class Meta:
        model= users
        fields=['firstName','lastName','idno','phone_No','address','country','email','is_student','is_sponsor','password']


        def create(self, validated_data):
            user = users(
                email=validated_data['email'],
                extra_kwargs = {'password': {'write_only': True}}
            )
            user.set_password(validated_data['password'])
            user.save()
            return user