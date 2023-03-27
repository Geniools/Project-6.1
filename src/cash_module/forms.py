from django import forms

from cash_module.models import CashTransaction
from base_app.models import Currency


# Custom form for CashTransactionAdmin
class CashTransactionForm(forms.ModelForm):
    amount = forms.FloatField()
    currency_type = forms.ModelChoiceField(queryset=Currency.objects.all())
    
    class Meta:
        model = CashTransaction
        fields = ('source', 'target', 'amount', 'currency_type')
