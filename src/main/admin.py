from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name')
    list_filter = ('is_staff', 'is_superuser',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    
    @admin.display(description='Full name')
    def full_name(self, obj):
        return obj.get_full_name()
    
    # Only superusers can access the User model in the admin panel
    def has_module_permission(self, request):
        return request.user.is_superuser
    
    def get_list_display(self, request):
        list_display = ['username', 'email', 'full_name']
        # If the user is a superuser, show all the fields
        if request.user.is_superuser:
            list_display += ['is_active', 'is_staff', 'is_superuser', 'is_treasurer']
            return tuple(list_display)
        
        if request.user.is_treasurer:
            list_display += ['is_treasurer']
            return tuple(list_display)
        
        # Otherwise, show only the username, email and full name fields
        return tuple(list_display)
    
    def get_readonly_fields(self, request, obj=None):
        # Define the read-only fields
        self.readonly_fields = ['date_joined', 'last_login']
        
        # If the user is not a superuser, add the first_name and last_name fields to the read-only fields
        if not request.user.is_superuser:
            self.readonly_fields += ['first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'is_treasurer', 'groups', 'user_permissions']
        
        return super().get_readonly_fields(request, obj)
    
    # Shows only the fields that a user which is not a superuser can view
    def get_fieldsets(self, request, obj=None):
        self.fieldsets = (
            ('General', {'fields': ('username', 'email',)}),
            ('Personal info', {'fields': ('first_name', 'last_name')}),
            ('Security info', {'fields': ('last_login', 'date_joined')}),
        )
        
        if request.user.is_superuser:
            self.fieldsets = (
                ('General', {'fields': ('username', 'email',)}),
                ('Personal info', {'fields': ('first_name', 'last_name')}),
                ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'is_treasurer', 'groups', 'user_permissions')}),
                ('Security info', {'fields': ('last_login', 'date_joined')}),
            )
        
        return super().get_fieldsets(request, obj)
    
    # Returning the users that are shown in the admin panel
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        
        # If the user is a superuser, return all users
        if request.user.is_superuser:
            return qs
        
        # Otherwise, return only the user that is logged in
        return qs.filter(username=request.user.username)
