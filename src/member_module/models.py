from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.IntegerField(primary_key=True,max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class LinkedTransaction(models.Model):
    id = models.IntegerField(primary_key=True, max_length=20)
    member_id=models.IntegerField(models.ForeignKey(Member, on_delete=models.DO_NOTHING),max_length=20)
    transaction_bank_reference=models.CharField(models.ForeignKey(base.app.Transaction, on_delete=DO_NOTHING),max_length=30)
