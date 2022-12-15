from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class orderItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'user')



admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
