from django.urls import path
from .views import RegisterAPIView, UserAPIView


urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('user/<int:pk>', UserAPIView.as_view(), name='user-detail'),
]