from django.contrib import admin
from django.contrib.admin import register
from base_app.models import Transaction, File, Category, Currency, BalanceDetails


# Register your models here.

@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

        return False


@register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@register(BalanceDetails)
class BalanceDetailsAdmin(admin.ModelAdmin):
    pass
