from django.contrib import admin
from .models import *


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ("username", )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "date_creation")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "product")

