from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display =['pkid','id', 'username', 'first_name', 'last_name','email', 'is_staff', 'is_active']
    list_display_link = ['id','email']
    list_filter = ['username', 'first_name', 'last_name','email','is_staff', 'is_active']
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields":("email","password",)
            },
        ),
        (
            _("Personal Information"),
            {
                "fields":('username', 'first_name', 'last_name','email',)
            },
        ),
        (
            _("Permission and Groups"),
            {
                "fields":('user_permissions','is_staff', 'is_active', 'is_superuser', 'groups')
            }
        )
    )
    