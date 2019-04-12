from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer, User, BudgetSerializer, Budget, TransactionSerializer, Transaction


# Create your views here.
class RegisterAPIView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.filter(id=self.kwargs['pk'])
        return user.values()


class BudgetListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)


class BudgetDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)


class TransactionListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        print( Transaction.objects.filter(budget__user__username=self.request.user.username))
        return Transaction.objects.filter(budget__user__username=self.request.user.username)