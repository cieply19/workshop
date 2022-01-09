from django.contrib import admin
from .models import Client, Car, Repair


class CarInLine(admin.StackedInline):
    model = Car
    max_num = 3


class RepairInLine(admin.TabularInline):
    model = Repair


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CarInLine,
    ]
    list_display = ["firstname", "lastname", "phone", "email"]
    search_fields = ["firstname", "lastname"]
    search_help_text = "Szukanie po dowolnym tekście"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [
        RepairInLine,
    ]
    list_display = ["car_brand", "brand_model", "year", "registration_number", "vin", "owner"]
    list_filter = ["car_brand", "brand_model"]
    search_fields = ("car_brand", "brand_model", "year", "vin", "registration_number", "owner__firstname",
                     "owner__lastname", "owner__phone")
    search_help_text = "Szukanie po dowolnym tekście"


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ["car",  "start_date","end_date", "description", "price", "owner"]
    list_filter = ["car", "end_date", "owner"]
    search_fields = ("car__car_brand", "car__brand_model", "description", "price")
    search_help_text = "Szukanie po dowolnym tekście"
