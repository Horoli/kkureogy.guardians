from django.contrib import admin
from . import models

@admin.register(models.Blog)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "author",
                    "title",
                    "text",
                    "pub_date",

                )
            },
        ),
    )