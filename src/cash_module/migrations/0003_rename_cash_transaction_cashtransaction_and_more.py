# Generated by Django 4.1.6 on 2023-03-21 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_delete_cashtransaction_alter_balancedetails_options_and_more'),
        ('cash_module', '0002_alter_cash_transaction_balance_details_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cash_Transaction',
            new_name='CashTransaction',
        ),
        migrations.AlterModelOptions(
            name='cashtransaction',
            options={'verbose_name': 'Cash Transaction', 'verbose_name_plural': 'Cash Transactions'},
        ),
    ]