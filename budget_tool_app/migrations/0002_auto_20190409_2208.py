# Generated by Django 2.2 on 2019-04-09 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_tool_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type_of',
            field=models.CharField(choices=[('withdrawal', 'Withdrawal'), ('deposit', 'Deposit')], default='withdrawal', max_length=48),
        ),
    ]
