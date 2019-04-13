from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer, User, BudgetSerializer, Budget, TransactionSerializer, Transaction


# Create your views here.
class RegisterAPIView(generics.CreateAPIView):
    """Defines the Registraion API endpoint view.
    
    Methods
        POST
            Args:
                username (str): required.
                email (str): required. Must be an address format. ex: example@example.com
                password (str): requried. Must meet password requirements.
                first_name (str): optional.
                last_name (str): optional.
    """

    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserAPIView(generics.RetrieveAPIView):
    """Defines the User API endpoint view.
    
    Methods
        GET
            *Must provide a valid user id in the url.
    """

    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        """Limits queryset to the user specified via the user id in the url."""
        user = User.objects.filter(id=self.kwargs['pk'])
        return user.values()


class BudgetListAPIView(generics.ListCreateAPIView):
    """Defines the Budget List API endpoint view.
        
    Methods
        GET
            Args:
                Token (str): required. Auth token provided to the user upon login.
        POST
            Args:
                Token (str): required. Auth token provided to the user upon login.
                name (str): required. Name of new budget category.
                budget_amount (int/float): required. Allocated budget amount.
    """

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """Limits queryset to budgets only relavent to the signed in user."""

        return Budget.objects.filter(user__username=self.request.user.username)

    def perform_create(self, serializer):
        """Saves a new budget to the database for the signed in user."""

        return serializer.save(user_id=self.request.user.id)


class BudgetDetailAPIView(generics.RetrieveAPIView):
    """Defines the Transaction List API endpoint view.
        
    Methods
        GET
            Args:
                Token (str): required. Auth token provided to the user upon login.
                *Must provide a valid budget id in the url.
    """

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """Limits queryset to the budget specified via the budget id in the url."""
        return Budget.objects.filter(user__username=self.request.user.username)


class TransactionListAPIView(generics.ListCreateAPIView):
    """Defines the Transaction List API endpoint view.
        
    Methods
        GET
            Args:
                Token (str): required. Auth token provided to the user upon login.
        POST
            Args:
                Token (str): required. Auth token provided to the user upon login.
                type_of (selection str): required. Selections are 'withdrawal' or 'deposit'.
                amount (int/float): required. Transaction amount.
                description (str): optional. Transaction details.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """Limits queryset to transactions only relavent to the signed in user and specified budget."""
        return Transaction.objects.filter(budget__user__username=self.request.user.username)

    def perform_create(self, serializer):
    """Saves a new transaction to the database for the signed in user and specified budget."""
        return serializer.save()

class TransactionDetailAPIView(generics.RetrieveAPIView):
    """Defines the Transaction List API endpoint view.
        
    Methods
        GET
            Args:
                Token (str): required. Auth token provided to the user upon login.
                *Must provide a valid budget id in the url.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """Limits queryset to the Transactions of the budget specified via the budget id in the url."""
        return Transaction.objects.filter(budget__user__username=self.request.user.username)
