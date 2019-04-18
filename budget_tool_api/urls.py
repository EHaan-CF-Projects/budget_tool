from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterAPIView, UserAPIView, BudgetListAPIView, BudgetDetailAPIView, TransactionListAPIView, TransactionDetailAPIView


urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('user/<int:pk>', UserAPIView.as_view(), name='user-detail'),
    path('login', views.obtain_auth_token),
    path('budgets/', BudgetListAPIView.as_view(), name='budget-list-api'),
    path('budgets/<int:pk>', BudgetDetailAPIView.as_view(), name='budget-detail-api'),
    path('transactions/', TransactionListAPIView.as_view(), name='transaction-list-api'),
    path('transactions/<int:pk>', TransactionDetailAPIView.as_view(), name='transaction-detail-api'),
]
