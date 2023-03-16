from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
	list_filter = ('is_staff', 'is_superuser', 'is_active')
	search_fields = ('username', 'email', 'first_name', 'last_name')
	ordering = ('username',)
	
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields':  ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
		}),
	)
	
	# Only superusers can access the User model in the admin panel
	def has_module_permission(self, request):
		return request.user.is_superuser
	
	def get_readonly_fields(self, request, obj=None):
		# Define the read-only fields
		self.readonly_fields = ['date_joined', 'last_login']
		
		# If the user is not a superuser, add the first_name and last_name fields to the read-only fields
		if not request.user.is_superuser:
			self.readonly_fields += ['first_name', 'last_name']
		
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
				('General', {'fields': ('username', 'email', 'is_active')}),
				('Personal info', {'fields': ('first_name', 'last_name')}),
				('Permissions', {'fields': ('is_superuser', 'is_staff', 'groups', 'user_permissions')}),
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
