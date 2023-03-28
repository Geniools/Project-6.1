from django.contrib import admin
from django.utils import timezone

from cash_module.models import CashTransaction
from base_app.models import BalanceDetails
from cash_module.forms import CashTransactionForm


@admin.register(CashTransaction)
class CashTransactionAdmin(admin.ModelAdmin):
    list_display = ('source', 'target', 'amount', 'currency_type')
    search_fields = ('source', 'target')
    form = CashTransactionForm
    
    @admin.display(description='amount')
    def amount(self, obj):
        return obj.balance_details_id.amount
    
    @admin.display(description='currency_type')
    def currency_type(self, obj):
        return obj.balance_details_id.currency_type_id
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        if obj:
            form.base_fields['amount'].initial = obj.balance_details_id.amount
            form.base_fields['currency_type'].initial = obj.balance_details_id.currency_type_id
        
        return form
    
    def save_model(self, request, obj, form, change):
        if obj.balance_details_id:
            balance_details = obj.balance_details_id
        else:
            balance_details = BalanceDetails()
            balance_details.date = timezone.now()
            obj.balance_details_id = balance_details
        
        balance_details.amount = form.cleaned_data['amount']
        balance_details.currency_type_id = form.cleaned_data['currency_type']
        balance_details.save()
        super().save_model(request, obj, form, change)
