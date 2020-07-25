from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    """Custom User admin for default User"""

    ordering = ["id"]
    list_display = ["email", "username", "is_staff"]
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
