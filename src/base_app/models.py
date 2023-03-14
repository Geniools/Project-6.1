from django.db import models


# Create your models here.

class Transaction(models.Model):
    bank_reference = models.CharField(max_length=30, null=False, primary_key=True)
    file_id = models.ForeignKey("base_app.File", on_delete=models.DO_NOTHING, null=False, related_name="file_id")
    balance_details_id = models.ForeignKey("base_app.File", on_delete=models.DO_NOTHING, null=False, related_name="balance_details_id")
    category_id = models.ForeignKey("base_app.Category", on_delete=models.DO_NOTHING, null=False)
    customer_reference = models.CharField(max_length=30, null=False)
    entry_date = models.DateField(null=False)
    guessed_entry_date = models.DateField(null=False)
    id = models.CharField(max_length=4, null=False)
    transaction_details = models.CharField(max_length=255, null=False)
    extra_details = models.CharField(max_length=255, null=False)
    funds_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.bank_reference}"


class File(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    available_closing_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, null=False,
                                                     related_name="available_closing_balance_id")
    final_closing_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, null=False, related_name="final_closing_balance_id")
    final_opening_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, null=False, related_name="final_opening_balance_id")
    final_available_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, null=False,
                                                   related_name="final_available_balance_id")
    account_identification = models.CharField(max_length=37, null=False)
    sequence_number = models.CharField(max_length=255, null=True)
    statement_number = models.CharField(max_length=255, null=True)
    transaction_reference_nr = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.id} : {self.account_identification}"


class CashTransaction(models.Model):
    pass


class Category(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.id} : {self.name}"


class Currency(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=3, null=False)

    def __str__(self):
        return f"{self.id} : {self.name}"


class BalanceDetails(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    amount = models.FloatField(null=False)
    currency_type = models.IntegerField(null=False)
    date = models.DateField(null=False)
    status = models.CharField(null=True, max_length=1, choices=(("C", "C"), ("D", "D"),))

    def __str__(self):
        return f"{self.id} : {self.dat}"
# Unsure if choices are correct
#
