from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, verbose_name="Email address")
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False, help_text="Designates that this user has all permissions without explicitly assigning them.")
    is_staff = models.BooleanField(default=True, help_text="Designates whether the user can log into this admin site.")
    is_active = models.BooleanField(default=True)
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

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return f"{self.first_name[0]}. {self.last_name}"

    # Defines the permissions that every user has
    def has_perm(self, perm, obj=None):
        # Every user has the permission to view and change users (permissions are defined in the admin.py file)
        if perm in ('main.change_user', 'main.view_user'):
            return True

        return super().has_perm(perm, obj)
