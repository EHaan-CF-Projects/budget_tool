from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm


# Create your views here.
class BudgetListView(LoginRequiredMixin, ListView):
    """Defines the Budget List View."""

    template_name = './budget_list.html'
    model = Budget
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """Renders list of user-specific budgets from the database."""
        return Budget.objects.filter(user__username=self.request.user.username)

class BudgetDetailView(LoginRequiredMixin, ListView):
    """Defines the Budget Detail View."""

    template_name = './budget_detail.html'
    model = Transaction
    context_object_name = 'transactions'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """Renders list of user-specific transaction from the database related to the signed-in user."""
        return Transaction.objects.all()

class BudgetCreateView(LoginRequiredMixin, CreateView):
    """Defines the Create New Budget View."""
    
    template_name = './create_budget.html'
    model = Budget
    form_class = BudgetForm
    success_url = reverse_lazy('budget_list')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validates the budget form."""
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransactionCreateView(LoginRequiredMixin, CreateView):
    """Defines the Create New Transaction View."""
    
    template_name = './create_transaction.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('budget_detail')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validates the Transaction form."""
        form.instance.user = self.request.user
        return super().form_valid(form)