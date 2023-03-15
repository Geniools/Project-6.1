from django.db import models


# Create your models here.

class Cash_Transaction(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    balance_details_id = models.IntegerField(models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING))
    source = models.CharField(max_length=50, null=False)
    target = models.CharField(max_length=50, null=False)