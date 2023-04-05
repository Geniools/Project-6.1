# Generated by Django 4.1.7 on 2023-04-05 08:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(blank=True, choices=[('C', 'C'), ('D', 'D')], help_text='C = Credit, D = Debit', max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Balance Details',
                'verbose_name_plural': 'Balance Details',
                'db_table': 'BalanceDetails',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
                'db_table': 'Currency',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_reference_nr', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16)])),
                ('related_reference_nr', models.CharField(max_length=16, null=True, validators=[django.core.validators.MinLengthValidator(16)])),
                ('account_identification', models.CharField(max_length=35)),
                ('statement_number', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None)])),
                ('sequence_number', models.CharField(max_length=5, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None)])),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
                ('available_balance_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='available_balance_id', to='base_app.balancedetails', verbose_name='Available Balance')),
                ('final_closing_balance_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='final_closing_balance_id', to='base_app.balancedetails', verbose_name='Final Closing Balance')),
                ('final_opening_balance_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='final_opening_balance_id', to='base_app.balancedetails', verbose_name='Final Opening Balance')),
                ('forward_available_balance_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='forward_available_balance_id', to='base_app.balancedetails', verbose_name='Forward Available Balance')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'db_table': 'File',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_reference', models.CharField(max_length=30)),
                ('custom_description', models.TextField(blank=True, null=True)),
                ('customer_reference', models.CharField(max_length=16, null=True)),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('guessed_entry_date', models.DateField(default=django.utils.timezone.now)),
                ('transaction_identification_code', models.CharField(max_length=4)),
                ('transaction_details', models.TextField()),
                ('extra_details', models.CharField(max_length=255)),
                ('funds_code', models.CharField(blank=True, max_length=1, null=True)),
                ('balance_details_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='balance_details_id', to='base_app.balancedetails', verbose_name='Balance Details')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base_app.category', verbose_name='Category')),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.file', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'Transaction',
            },
        ),
        migrations.AddField(
            model_name='balancedetails',
            name='currency_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base_app.currency', verbose_name='Currency'),
        ),
    ]
