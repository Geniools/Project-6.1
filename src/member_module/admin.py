from django.contrib import admin

from member_module.models import Member, LinkedTransaction


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(LinkedTransaction)
class LinkedTransaction(admin.ModelAdmin):
    list_display = ('member_id', 'transaction_bank_reference')
    list_filter = ('member_id', 'transaction_bank_reference')
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
