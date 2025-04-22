from django.contrib import admin
from . models import Product,Variation

# Register your models here.
class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id','name','description','price_marketing','type',
    inlines = VariationInline,


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    
    list_display = 'name','product','price','price_promotional','stock',