from django.test import TestCase, Client
from budget_tool_project.factories import UserFactory, BudgetFactory, TransactionFactory, Budget, Transaction


class TestBudgetViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'<h2>Sign In:</h2>', res.content)
    
    def test_view_if_logged_in(self):
        self.c.login(username=self.user.username, password='password')
        budget = BudgetFactory(user=self.user)
        res = self.c.get('/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'<h1>Create New Budget</h1>', res.content)

    def test_only_owned_budget_list(self):
        self.c.login(username=self.user.username, password='password')
        own_budget = BudgetFactory(user=self.user)
        other_budget = BudgetFactory()
        res = self.c.get('/budget', follow=True)
        self.assertIn(own_budget.name.encode(), res.content)
        self.assertNotIn(other_budget.name.encode(), res.content)

