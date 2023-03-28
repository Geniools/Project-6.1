from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator
from django.utils.timezone import now


class File(models.Model):
    id = models.AutoField(primary_key=True)
    # Tag :64: (Optional)
    available_balance_id = models.OneToOneField(
        "base_app.BalanceDetails", on_delete=models.PROTECT, related_name="available_balance_id", verbose_name="Available Balance", null=True
    )
    # Tag :62F: (Mandatory)
    final_closing_balance_id = models.OneToOneField(
        "base_app.BalanceDetails", on_delete=models.PROTECT, related_name="final_closing_balance_id", verbose_name="Final Closing Balance"
    )
    # Tag :60F: (Mandatory)
    final_opening_balance_id = models.OneToOneField(
        "base_app.BalanceDetails", on_delete=models.PROTECT, related_name="final_opening_balance_id", verbose_name="Final Opening Balance"
    )
    # Tag :65: (Optional)
    forward_available_balance_id = models.OneToOneField(
        "base_app.BalanceDetails", on_delete=models.PROTECT, related_name="forward_available_balance_id", verbose_name="Forward Available Balance", null=True
    )
    # Tag :20: (Mandatory)
    transaction_reference_nr = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    # Tag :21: (Optional)
    related_reference_nr = models.CharField(max_length=16, validators=[MinLengthValidator(16)], null=True)
    # Tag :25: (Mandatory)
    account_identification = models.CharField(max_length=35)
    # Tag :28C: (statement number) (Mandatory)
    statement_number = models.CharField(validators=[int_list_validator(sep="", allow_negative=False)], max_length=5)
    # Tag :28C: (sequence number) (Optional)
    sequence_number = models.CharField(validators=[int_list_validator(sep="", allow_negative=False)], max_length=5, null=True)
    # Registration time of the file (no tag in the MT940 file)
    registration_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        db_table = "File"
    
    def __str__(self):
        return f"ID: {self.id} : Identification: {self.account_identification}"


# Representation of the :61: tag
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    bank_reference = models.CharField(max_length=30)
    file_id = models.ForeignKey("base_app.File", on_delete=models.CASCADE, verbose_name="File")
    balance_details_id = models.OneToOneField("base_app.BalanceDetails", on_delete=models.PROTECT, related_name="balance_details_id", verbose_name="Balance Details")
    category_id = models.ForeignKey("base_app.Category", on_delete=models.PROTECT, verbose_name="Category", null=True, blank=True)
    custom_description = models.TextField(max_length=255, null=True, blank=True)
    customer_reference = models.CharField(max_length=16, null=True)
    entry_date = models.DateField(default=now)
    guessed_entry_date = models.DateField(default=now)
    transaction_identification_code = models.CharField(max_length=4)
    # Tag :86:
    transaction_details = models.TextField()
    extra_details = models.CharField(max_length=255)
    funds_code = models.CharField(max_length=1, null=True, blank=True)
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        db_table = "Transaction"
    
    def __str__(self):
        return self.bank_reference


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "Category"
    
    def __str__(self):
        return f"{self.name}"


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    # A currency code is a three-letter code in ISO 4217.
    name = models.CharField(max_length=3, validators=[MinLengthValidator(3)], unique=True)
    
    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        db_table = "Currency"
    
    def save(self, *args, **kwargs):
        # Convert the currency name to uppercase
        self.name = self.name.upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class BalanceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    currency_type_id = models.ForeignKey(Currency, on_delete=models.PROTECT, verbose_name="Currency")
    date = models.DateField(default=now)
    status = models.CharField(null=True, blank=True, max_length=1, choices=(("C", "C"), ("D", "D"),), help_text="C = Credit, D = Debit")
    
    class Meta:
        verbose_name = "Balance Details"
        verbose_name_plural = "Balance Details"
        db_table = "BalanceDetails"
    
    def __str__(self):
        return f"Amount: {self.amount}; Date: {self.date}"
