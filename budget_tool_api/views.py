from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .serializer import UserSerializer, User


# Create your views here.
class RegisterAPIView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication)
    serializer_class = UserSerializer


class UserAPIView(generics.CreateAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.filter(id=self.kwargs['pk'])


