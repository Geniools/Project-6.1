import datetime

from django.db import models
from django.core.validators import MinLengthValidator

from django.utils.timezone import now


class Transaction(models.Model):
    bank_reference = models.CharField(max_length=30, primary_key=True)
    balance_details_id = models.OneToOneField("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="balance_details_id")
    category_id = models.ForeignKey("base_app.Category", on_delete=models.DO_NOTHING)
    customer_reference = models.CharField(max_length=30)
    entry_date = models.DateField(default=now)
    guessed_entry_date = models.DateField(default=now)
    id = models.CharField(max_length=4)
    transaction_details = models.CharField(max_length=255)
    extra_details = models.CharField(max_length=255)
    funds_code = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        db_table = "Transaction"

    def __str__(self):
        return f"{self.bank_reference}"


class File(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_id = models.ForeignKey("base_app.Transaction", on_delete=models.DO_NOTHING)
    available_closing_balance_id = models.OneToOneField("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="available_closing_balance_id")
    final_closing_balance_id = models.OneToOneField("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="final_closing_balance_id")
    final_opening_balance_id = models.OneToOneField("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="final_opening_balance_id")
    final_available_balance_id = models.OneToOneField("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="final_available_balance_id")
    account_identification = models.CharField(max_length=37)
    sequence_number = models.CharField(max_length=255, null=True)
    statement_number = models.CharField(max_length=255, null=True)
    transaction_reference_nr = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        db_table = "File"

    def __str__(self):
        return f"{self.id} : {self.account_identification}"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "Category"

    def __str__(self):
        return f"{self.id} : {self.name}"


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    # A currency code is a three-letter code in ISO 4217.
    name = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        db_table = "Currency"

    def __str__(self):
        return f"{self.id} : {self.name}"


class BalanceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    currency_type = models.OneToOneField(Currency, on_delete=models.DO_NOTHING)
    date = models.DateField(default=now)
    status = models.CharField(null=True, max_length=1, choices=(("C", "C"), ("D", "D"),))

    class Meta:
        verbose_name = "Balance Details"
        verbose_name_plural = "Balance Details"
        db_table = "BalanceDetails"

    def __str__(self):
        return f"{self.id} : {self.date}"
