from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated

import jwt
from django.conf import settings

from user_api.serializers import CustomUserSerializer
from user_api.serializers import CustomTokenObtainPairSerializer



class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return Response({'detail': 'Logged in successfully'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)




class LoginAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)