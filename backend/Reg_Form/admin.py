from django.contrib import admin
from .models import users


@admin.register(users)
class UserAdmin(admin.ModelAdmin):
    list_display: tuple[str] = (
        "id", "Fullname", "email", "College", "PhoneNo", "event")

    search_fields: tuple[str] = ("Fullname", "event", "College")

    list_filter: tuple[str] = ("event", "College")
