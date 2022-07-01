from django.contrib import admin
from .models import Category, Customer, Product, Order

# Register your models here.
@admin.register(Category)
class Request_category(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Customer)
class Request_customer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']

@admin.register(Product)
class Request_products(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']

@admin.register(Order)
class Request_orders(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status']