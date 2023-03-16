from django.db import models


# Create your models here.

class Cash_Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    balance_details_id = models.ForeignKey("base_app.BalanceDetails", on_delete=models.DO_NOTHING)
    source = models.CharField(max_length=50)
    target = models.CharField(max_length=50)