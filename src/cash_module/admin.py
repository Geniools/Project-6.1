from django.contrib import admin

from cash_module.models import CashTransaction


@admin.register(CashTransaction)
class CashTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'target')
