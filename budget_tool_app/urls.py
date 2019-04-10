from django.urls import path
from .views import BudgetListView, BudgetDetailView, BudgetCreateView, TransactionCreateView

urlpatterns = [
    path('', BudgetListView.as_view(), name='budget_list'),
    path('<int:pk>', BudgetDetailView.as_view(), name='budget_detail'),
    path('add', BudgetCreateView.as_view(), name='budget_add'),
    path('<int:pk>/transaction/add', TransactionCreateView.as_view(), name='transaction_add'),
]