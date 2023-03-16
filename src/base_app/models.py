from django.db import models


class Transaction(models.Model):
    bank_reference = models.CharField(max_length=30, primary_key=True)
    file_id = models.ForeignKey("base_app.File", on_delete=models.DO_NOTHING, related_name="file_id")
    balance_details_id = models.ForeignKey("base_app.File", on_delete=models.DO_NOTHING, related_name="balance_details_id")
    category_id = models.ForeignKey("base_app.Category", on_delete=models.DO_NOTHING)
    customer_reference = models.CharField(max_length=30)
    entry_date = models.DateField()
    guessed_entry_date = models.DateField()
    id = models.CharField(max_length=4)
    transaction_details = models.CharField(max_length=255)
    extra_details = models.CharField(max_length=255)
    funds_code = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.bank_reference}"


class File(models.Model):
    id = models.AutoField(primary_key=True)
    available_closing_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="available_closing_balance_id")
    final_closing_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="final_closing_balance_id")
    final_opening_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="final_opening_balance_id")
    final_available_balance_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING, related_name="final_available_balance_id")
    account_identification = models.CharField(max_length=37)
    sequence_number = models.CharField(max_length=255, null=True)
    statement_number = models.CharField(max_length=255, null=True)
    transaction_reference_nr = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        return f"{self.id} : {self.account_identification}"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.id} : {self.name}"


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=3)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.id} : {self.name}"


class BalanceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    currency_type = models.IntegerField()
    date = models.DateField()
    status = models.CharField(null=True, max_length=1, choices=(("C", "C"), ("D", "D"),))

    class Meta:
        verbose_name = "Balance Details"
        verbose_name_plural = "Balance Details"

    def __str__(self):
        return f"{self.id} : {self.date}"
