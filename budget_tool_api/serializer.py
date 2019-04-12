from django.contrib.auth.models import User
from budget_tool_app.models import Budget, Transaction
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'].lower(),
            'email': validated_data['email'],
        })

        user.set_password([validated_data['password']])
        user.save()
        return user


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Budget
        fields = ('id', 'owner', 'user', 'name', 'total_budget')


class TransactionSerializer(serializers.HyperlinkedRelatedField):
    budget = serializers.HyperlinkedRelatedField(view_name='budget-detail-api', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'budget', 'type_of', 'amount', 'description')
