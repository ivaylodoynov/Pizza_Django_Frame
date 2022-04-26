from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from Pizza_Django_Framework.accounts.models import PizzaUser

UserModel = get_user_model()

@admin.register(UserModel)
class PizzaUserAdmin(UserAdmin):
    list_display = ("email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "groups")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions",{
            "fields": (
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"),
            }),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )