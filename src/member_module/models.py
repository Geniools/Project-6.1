from django.db import models


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    
    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        db_table = "Member"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LinkedTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name="Member")
    transaction_bank_reference = models.OneToOneField("base_app.Transaction", on_delete=models.PROTECT, max_length=30, verbose_name="Transaction")
    
    class Meta:
        verbose_name = "Linked Transaction"
        verbose_name_plural = "Linked Transactions"
        db_table = "LinkedTransaction"
    
    def __str__(self):
        return f"{self.member_id} {self.transaction_bank_reference}"
