from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Budget(models.Model):
    """Budget Databse:
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
    """

    TYPES = [
        ('withdrawal', 'Withdrawal'),
        ('deposit', 'Deposit'),
    ]

    budget = models.ForeignKey(Budget, related_name='transactions', null=True, on_delete=models.CASCADE)
    type_of = models.CharField(choices=TYPES, default='available', max_length=48)
    amount = models.FloatField(0.00)
    description = models.CharField(max_length=256)

    def __repr__(self):
        return f'<Transaction: {self.type_of} of {self.amount}>'

    def __str__(self):
        return f'Transaction: {self.type_of} of {self.amount}'