from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterAPIView, UserAPIView, BudgetListAPIView, BudgetDetailAPIView, TransactionListAPIView


urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('user/<int:pk>', UserAPIView.as_view(), name='user-detail'),
    path('login', views.obtain_auth_token),
    path('budget_list/', BudgetListAPIView.as_view(), name='budget-list-api'),
    path('budget_detail/<int:pk>', BudgetDetailAPIView.as_view(), name='budget-detail-api'),
    path('transaction_list/', TransactionListAPIView.as_view(), name='transaction-list-api'),
]
