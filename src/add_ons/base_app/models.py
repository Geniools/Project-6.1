from django.db import models


# Create your models here.

class Transaction(models.Model):
	bank_reference = models.CharField(max_length=30, null=False, primary_key=True)
	file_id = models.ForeignKey("base_app.File", on_delete=models.DO_NOTHING)
	entry_date = models.DateField()
	transaction_details = models.CharField(max_length=255, null=False)


class File(models.Model):
	pass
