# Generated by Django 4.1.7 on 2023-04-05 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=50)),
                ('target', models.CharField(max_length=50)),
                ('balance_details_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='base_app.balancedetails', verbose_name='Balance Details')),
            ],
            options={
                'verbose_name': 'Cash Transaction',
                'verbose_name_plural': 'Cash Transactions',
                'db_table': 'CashTransaction',
            },
        ),
    ]
