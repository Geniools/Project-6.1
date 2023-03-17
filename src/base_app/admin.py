from django.contrib import admin

from base_app.models import Transaction, File, Category, BalanceDetails, Currency


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('entry_date', 'category_id')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'account_identification')

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


@admin.register(BalanceDetails)
class BalanceDetailsAdmin(admin.ModelAdmin):
    list_display = ('amount', 'currency_type', 'date', 'status')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
