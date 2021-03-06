
from users.models import  users
from.serializers import UserCreationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

class UserCreation(APIView):

    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
            user=users.objects.all()
            serializer=UserCreationSerializer(user,many=True)
            return Response(serializer.data)

    def post(self,request, format=None):
        
        serializer=UserCreationSerializer(data=request.data)

        if serializer.is_valid():
            password=make_password(self.request.data.get('password'))
            
            
            serializer.save(password=password)
            
            return Response(serializer.data)
        return Response(serializer.errors)