import factory
from django.contrib.auth.models import User
from budget_tool_app.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    """Instantiates a guinea pig user."""
    
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """Instantiates a test budget."""

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    total_budget = 42


class TransactionFactory(factory.django.DjangoModelFactory):
    """Instantiates a test transaction."""

    class Meta:
        model = Transaction

    budget = factory.SubFactory(BudgetFactory)
    type_of = 'withdrawal'
    amount = 42
    description = factory.Faker('paragraph')
    
