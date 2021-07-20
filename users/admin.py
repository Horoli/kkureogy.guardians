from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "phone_number",
                    "birthdate",
                    "country",
                    "volunteer_portal_ID",
                    "bio",
                )
            },
        ),
    )