from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    class meta:
        model = Budget
        fields = ['name', 'total_budget']

class TransactionForm(ModelForm):
    class meta:
        model = Transaction
        fields = ['budget', 'type_of', 'amount', 'description']
