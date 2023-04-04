from django.db import models


class CashTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    balance_details_id = models.OneToOneField("base_app.BalanceDetails", on_delete=models.DO_NOTHING, verbose_name="Balance Details")
    source = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Cash Transaction"
        verbose_name_plural = "Cash Transactions"
        db_table = "CashTransaction"
    
    def __str__(self):
        if hasattr(self, "balance_details_id"):
            return f"{self.source} -> {self.target}: {self.balance_details_id}"
        else:
            return f"{self.source} -> {self.target}"
