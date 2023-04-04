from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, help_text="Unique username for the user. Is used to log in.")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, verbose_name="Email address")
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False, help_text="Designates that this user has all permissions without explicitly assigning them.")
    is_staff = models.BooleanField(default=True, help_text="Designates whether the user can log into this admin site.")
    is_active = models.BooleanField(default=True, help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.")
    is_treasurer = models.BooleanField(default=False, help_text="Designates whether the user can upload a transaction (MT940 file).")
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, help_text="Specific permissions for this user.")
    groups = models.ManyToManyField('auth.Group', blank=True, help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.")
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "User"
    
    def __str__(self):
        return f"{self.username}"
    
    def save(self, *args, **kwargs):
        # A superuser has the permission of a treasurer
        if self.is_superuser:
            self.is_treasurer = True
        
        super().save(*args, **kwargs)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return f"{self.first_name[0]}. {self.last_name}"
    
    def has_perm(self, perm, obj=None):
        # Default view permissions - should be available for every user
        view_permissions = (
            'main.view_user', 'base_app.view_transaction', 'base_app.view_file', 'base_app.view_balancedetails', 'base_app.view_category', 'base_app.view_currency',
            'member_module.view_member', 'member_module.view_linkedtransaction', 'cash_module.view_cashtransaction'
        )
        # Default change permissions - should be available for treasurers
        change_permissions = (
            'base_app.change_transaction', 'member_module.change_member', 'member_module.change_linkedtransaction',
            'cash_module.change_cashtransaction'
        )
        # Default add permissions - should be available for treasurers
        add_permissions = (
            'base_app.add_balancedetails', 'base_app.add_category', 'base_app.add_currency', 'member_module.add_member',
            'member_module.add_linkedtransaction', 'cash_module.add_cashtransaction'
        )
        # Other default permissions - available to every user
        other_default_permissions = ('main.change_user',)
        
        if perm in view_permissions or perm in other_default_permissions:
            return True
        
        if perm in change_permissions:
            return self.is_treasurer
        
        if perm in add_permissions:
            return self.is_treasurer
        
        return super().has_perm(perm, obj)
    
    def has_module_perms(self, app_label):
        # Gives every user access to the following apps
        if app_label in ('base_app', 'member_module', 'cash_module'):
            return True
        
        return super().has_module_perms(app_label)
