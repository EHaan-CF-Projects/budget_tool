from django.test import TestCase
from budget_tool_project.factories import UserFactory, BudgetFactory, TransactionFactory


class TestBudgetModel(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(name='test name', total_budget=42)
    
    def test_budget_attributes(self):
        self.assertEqual(self.budget.name, 'test name')
        self.assertEqual(self.budget.total_budget, 42)

class TestTransactionModel(TestCase):
    def setUp(self):
        self.transaction = TransactionFactory(type_of='withdrawal', amount=42, description='test description')
    
    def test_transaction_attributes(self):
        self.assertEqual(self.transaction.type_of, 'withdrawal')
        self.assertEqual(self.transaction.amount, 42)
        self.assertEqual(self.transaction.description, 'test description')

