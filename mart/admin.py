from django.contrib import admin
from .models import Product, Order, Cart, CartItem, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')






admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Cart)
