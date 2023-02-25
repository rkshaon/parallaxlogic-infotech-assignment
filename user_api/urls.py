from django.urls import path
from user_api.views import RegistrationAPIView, LoginAPIView



urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
