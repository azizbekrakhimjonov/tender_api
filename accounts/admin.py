from django.contrib import admin
from .models import Profil, FreightOrder


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    search_fields = ("username", "email")
    list_filter = ("email",)


@admin.register(FreightOrder)
class FreightOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cargo_description",
        "origin",
        "destination",
        "weight_kg",
        "volume_m3",
        "pickup_date",
        "delivery_date",
        "vehicle_type",
        "incoterms",
        "status",
        "created_at",
    )
    search_fields = ("cargo_description", "origin", "destination")
    list_filter = ("vehicle_type", "incoterms", "status", "pickup_date", "delivery_date")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "pickup_date"
