from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class LinkedTransaction(models.Model):
    id = models.IntegerField(primary_key=True)
    member_id= models.ForeignKey(Member, on_delete=models.DO_NOTHING, max_length=20)
    transaction_bank_reference=models.ForeignKey(base_app.Transaction, on_delete=models.DO_NOTHING,max_length=30)
