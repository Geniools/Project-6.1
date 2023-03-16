from django.db import models


class CashTransaction(models.Model):
    id = models.IntegerField(primary_key=True)
    balance_details_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING)
    source = models.CharField(max_length=50)
    target = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Cash Transaction"
        verbose_name_plural = "Cash Transactions"

    def __str__(self):
        return f"{self.id} : {self.source} -> {self.target}"
