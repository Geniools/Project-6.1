from django.contrib import admin

from base_app.models import Transaction, File, Category, BalanceDetails, Currency


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'entry_date', 'category_id', 'balance_details_id')
    list_filter = ('file_id', 'entry_date', 'category_id')
    search_fields = ('file_id', 'entry_date', 'category_id', 'transaction_details', 'extra_details')
    # Every field is readonly, except for category_id (as it should be manually changed)
    readonly_fields = (
        'bank_reference', 'file_id', 'balance_details_id', 'customer_reference', 'entry_date', 'guessed_entry_date', 'id', 'transaction_details', 'extra_details',
        'funds_code'
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('account_identification', 'transaction_reference_nr', 'statement_number', 'sequence_number')
    list_filter = ('account_identification',)
    search_fields = ('account_identification', 'transaction_reference_nr', 'statement_number', 'sequence_number')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(BalanceDetails)
class BalanceDetailsAdmin(admin.ModelAdmin):
    list_display = ('currency_type_id', 'amount', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('status', 'date')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
