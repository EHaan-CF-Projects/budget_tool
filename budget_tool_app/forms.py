from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """Establishes a form to create a new budget."""
    class Meta:
        model = Budget
        fields = ['name', 'total_budget']

class TransactionForm(ModelForm):
    """Establishes a form to create a new transaction."""
    class Meta:
        model = Transaction
        fields = ['type_of', 'amount', 'description']
