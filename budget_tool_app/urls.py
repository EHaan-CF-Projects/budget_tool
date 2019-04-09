from django.urls import path
from .views import BudgetListView, BudgetDetailView

urlpatterns = [
    path('', BudgetListView.as_view(), name='budget_list'),
    path('<int:id>', BudgetDetailView.as_view(), name='budget_detail'),
]