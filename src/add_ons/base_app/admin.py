from django.contrib import admin
from django.contrib.admin import register

from base_app.models import Transaction


# Register your models here.

@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		if request.user.is_superuser:
			return True
		
		return False
