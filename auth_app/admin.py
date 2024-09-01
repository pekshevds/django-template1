from django.contrib import admin
from auth_app.models import User
from auth_app.models import Pin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "id",
        "is_active",
    )


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
