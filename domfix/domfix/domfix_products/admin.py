from django.contrib import admin

from domfix.domfix_products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
