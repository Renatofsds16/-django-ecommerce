from django.contrib import admin
from . models import Order,ItemOrder

# Register your models here.


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = ItemOrderInline,


@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    ...
