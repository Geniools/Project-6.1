from django.contrib import admin

from member_module.models import Member, LinkedTransaction


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(LinkedTransaction)
class LinkedTransaction(admin.ModelAdmin):
    list_display = ('member_id', 'transaction_bank_reference')
