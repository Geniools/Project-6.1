from django.db import models


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        db_table = "Member"

    def __str__(self):
        return self.email


class LinkedTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    transaction_bank_reference = models.OneToOneField("base_app.Transaction", on_delete=models.DO_NOTHING, max_length=30)

    class Meta:
        verbose_name = "Linked Transaction"
        verbose_name_plural = "Linked Transactions"
        db_table = "LinkedTransaction"

    def __str__(self):
        return self.id
