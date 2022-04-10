from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'category', 'description', 'price', 'stock', 'is_available', 'modified_date')
    list_filter = ('category', 'stock', 'is_available')
    search_fields = ('product_name', 'category__category_name')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
