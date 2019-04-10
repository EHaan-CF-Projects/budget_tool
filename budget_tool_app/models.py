from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Budget(models.Model):
    """Budget Databse:

    Parameters:
        user (ForeignKey): relationship to a user.
        name (str): name of the budget.
        total_budget (float): budget amount.
        remaining_budget (float): budget amount after a given transaction.
    """

    user = models.ForeignKey(User, related_name='budgets', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=48)
    total_budget = models.FloatField()

    @property
    def remaining_budget(self):
        return 12

    def __repr__(self):
        return f'<Budget: {self.name} | {self.total_budget}>'

    def __str__(self):
        return f'Budget: {self.name} | {self.total_budget}'
    
class Transaction(models.Model):
    """Transaction Database:

    Parameters:
        budget (ForeignKey): relationship to a budget.
        type_of (choice): options for 'withdrawal' or 'deposit'.
        amount (float): transaction amount.
        description (str): brief summary of transaction.
    """

    TYPES = [
        ('withdrawal', 'Withdrawal'),
        ('deposit', 'Deposit'),
    ]

    budget = models.ForeignKey(Budget, related_name='transactions', null=True, on_delete=models.CASCADE)
    type_of = models.CharField(choices=TYPES, default='withdrawal', max_length=48)
    amount = models.FloatField(0.00)
    description = models.CharField(max_length=256)

    def __repr__(self):
        return f'<Transaction: {self.type_of} of {self.amount}>'

    def __str__(self):
        return f'Transaction: {self.type_of} of {self.amount}'