from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Budget, Transaction


# Create your views here.
class BudgetListView(LoginRequiredMixin, ListView):
    """Defines the Budget List View."""

    template_name = './budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """Renders list of user-specific budgets from the database."""
        return Budget.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        """Obtains list of user-specific budgets related to the signed-in user."""
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
        return context

class BudgetDetailView(LoginRequiredMixin, ListView):
    """Defines the Budget Detail View"""

    template_name = './budget_detail.html'
    model = Transaction
    context_object_name = 'transactions'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """Renders list of user-specific transaction from the database related to the signed-in user."""
        return Transaction.objects.filter(budget__user__username=self.request.user.username)