from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
