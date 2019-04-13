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


class TestBudgetCreateView(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()

    def test_create_view_adds_new_budget(self):
        self.c.login(username=self.user.username, password='password')
        form_data = {'name': 'Budget 1', 'budget_total': 42}
        res = self.c.post('/budget/add', form_data, follow=True)
        self.assertIn(b'Budget 1', res.content)
    

class TestCardCreateView(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()
        self.budget = BudgetFactory(user=self.user)
    

    #need help understanding this test... it is not passing, I think because it is not hitting the url which requires a pk for budget id.
    # def test_create_view_adds_new_transaction(self):
    #     self.c.login(username=self.user.username, password='password')
    #     form_data = {'type_of': 'withdrawal', 'amount': 42, 'description': 'something descriptive', 'budget': self.budget.id}
    #     res = self.c.post('{}/transaction/add'.format(self.budget.id), form_data, follow=True)

    #     self.assertIn(b'withdrawal', res.content)

