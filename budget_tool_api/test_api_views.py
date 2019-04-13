from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from budget_tool_app.models import Budget, Transaction
from budget_tool_api.views import BudgetListAPIView, TransactionListAPIView
import json


class TestUserAPI(TestCase):
    # need help understanding why I get 404 instead of 201
    def test_user_registration(self):
        user = {
            'username': 'test_user',
            'email': 'test@test.com',
            'password': 'password_test',
        }
        response = self.client.post('api/v1/register', user)

        self.assertEqual(response.status_code, 201)
        self.assertIn(b'"username": "test_user"', response.content)

    # need to solve above probelm for all other tests to be closer to working
    def test_user_login(self):
        user = {
            'username': 'test_user',
            'email': 'test@test.com',
            'password': 'password_test',
        }
        self.client.post('api/v1/register', user)
        response = self.client.post('api/v1/login', user)
        token = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(token['token']), 40)

class TestBudetAPI(APITestCase):
    def test_get_budget_api(self):
        user = {
            'username': 'test_user',
            'email': 'test@test.com',
            'password': 'password_test',
        }
        self.client.post('api/v1/register', user)
        response = self.client.post('api/v1/login', user)
        user = User.objects.get(username='test_user')
        view = BudgetListAPIView.as_view()
        factory = APIRequestFactory()
        request = factory.get('/api/v1/budget_list')
        force_authenticate(request, user=user, token=user.auth_token)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Budget.objects.all()), 0)


# class TestTransactionAPI(APITestCase):

