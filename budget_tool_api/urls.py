from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterAPIView, UserAPIView


urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('user/<int:pk>', UserAPIView.as_view(), name='user-detail'),
    path('login', views.obtain_auth_token),
]