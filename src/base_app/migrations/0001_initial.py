# Generated by Django 4.1.6 on 2023-03-14 15:22

from django.db import migrations, models
import django.db.models.deletion


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
                ('currency_type', models.IntegerField()),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('C', 'C'), ('D', 'D')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CashTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_identification', models.CharField(max_length=37)),
                ('sequence_number', models.CharField(max_length=255, null=True)),
                ('statement_number', models.CharField(max_length=255, null=True)),
                ('transaction_reference_nr', models.CharField(max_length=255, null=True)),
                ('available_closing_balance_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='available_closing_balance_id', to='base_app.balancedetails')),
                ('final_available_balance_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='final_available_balance_id', to='base_app.balancedetails')),
                ('final_closing_balance_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='final_closing_balance_id', to='base_app.balancedetails')),
                ('final_opening_balance_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='final_opening_balance_id', to='base_app.balancedetails')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('bank_reference', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('customer_reference', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('guessed_entry_date', models.DateField()),
                ('id', models.CharField(max_length=4)),
                ('transaction_details', models.CharField(max_length=255)),
                ('extra_details', models.CharField(max_length=255)),
                ('funds_code', models.CharField(max_length=50, null=True)),
                ('balance_details_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='balance_details_id', to='base_app.file')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base_app.category')),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='file_id', to='base_app.file')),
            ],
        ),
    ]
