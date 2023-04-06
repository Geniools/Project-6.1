from django.contrib import admin

from member_module.models import Member, LinkedTransaction


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            self.readonly_fields = ('first_name', 'last_name')
        
        return super().get_readonly_fields(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_treasurer or request.user.is_superuser


@admin.register(LinkedTransaction)
class LinkedTransaction(admin.ModelAdmin):
    list_display = ('member_id', 'transaction_bank_reference')
    list_filter = ('member_id',)
    search_fields = (
        'member_id__first_name', 'member_id__last_name', 'transaction_bank_reference__bank_reference', 'transaction_bank_reference__transaction_details',
        'transaction_bank_reference__extra_details', 'transaction_bank_reference__custom_description'
    )
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return False
