from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from user_api.serializers import CustomUserSerializer



class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return Response({'detail': 'Logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)