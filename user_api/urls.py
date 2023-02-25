from django.urls import path
from user_api import views



urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('profile/', views.ProfileAPIView.as_view(), name='profile'),
]
