from django.contrib import admin

from base_app.models import Transaction, File, Category, BalanceDetails, Currency


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('account_identification', 'transaction_reference_nr', 'statement_number', 'sequence_number')
    list_filter = ('account_identification',)
    search_fields = (
        'account_identification', 'transaction_reference_nr', 'statement_number', 'sequence_number', 'related_reference_nr',
        'available_balance_id__amount', 'available_balance_id__currency_type_id__name', 'available_balance_id__status',
        'final_closing_balance_id__amount', 'final_closing_balance_id__currency_type_id__name', 'final_closing_balance_id__status',
        'final_opening_balance_id__amount', 'final_opening_balance_id__currency_type_id__name', 'final_opening_balance_id__status',
        'forward_available_balance_id__amount', 'forward_available_balance_id__currency_type_id__name', 'forward_available_balance_id__status',
    )
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'entry_date', 'category_id', 'balance_details_id')
    list_filter = ('file_id', 'entry_date', 'category_id')
    search_fields = ('file_id__id', 'entry_date', 'category_id__name', 'transaction_details', 'extra_details', 'custom_description')
    # Every field is readonly, except for category_id and custom_description (as they should be manually changed)
    readonly_fields = (
        'bank_reference', 'file_id', 'balance_details_id', 'customer_reference', 'entry_date', 'guessed_entry_date', 'transaction_identification_code',
        'transaction_details', 'extra_details', 'funds_code'
    )
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(BalanceDetails)
class BalanceDetailsAdmin(admin.ModelAdmin):
    list_display = ('currency_type_id', 'amount', 'date', 'status')
    list_filter = ('status', 'date', 'currency_type_id')
    search_fields = ('status', 'date')
    empty_value_display = '-Manual-'
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
