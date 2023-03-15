from django.contrib import admin
from .models import Member
from .models import LinkedTransaction

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(LinkedTransaction)
class LinkedTransaction(admin.ModelAdmin):
    pass

