from django.db import models


# Create your models here.

class Transaction(models.Model):
    bank_reference = models.CharField(max_length=30, null=False, primary_key=True)
    file_id = models.ForeignKey("base_app.File", on_delete=models.DO_NOTHING, null=False)
    balance_details_id = models.ForeignKey("base_app.File", on_delete=models.DO_NOTHING, null=False)
    category_id = models.ForeignKey("base_app.Category", on_delete=models.DO_NOTHING, null=False)
    customer_reference = models.CharField(max_length=30, null=False)
    entry_date = models.DateField(null=False)
    guessed_entry_date = models.DateField(null=False)
    id = models.CharField(max_length=4, null=False)
    transaction_details = models.CharField(max_length=255, null=False)
    extra_details = models.CharField(max_length=255, null=False)
    funds_code = models.CharField(max_length=50, null=True)


class File(models.Model):
    pass


class CashTransaction(models.Model):
    pass


class Category(models.Model):
    id = models.AutoField(null=False, primary_key=False)
    name = models.CharField(max_length=30, null=False)


class Currency(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=3, null=False)


class BalanceDetails(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    amount = models.FloatField(null=False)
    currency_type = models.IntegerField(null=False)
    date = models.DateField(null=False)
    status = models.CharField(null=True, max_length=1, choices=("c", "d"))
# Unsure if capital C & D should be allowed or if a capital is mandatory
#
# Start and finish the File models. Register models through admin file
