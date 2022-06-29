from django.contrib import admin
from .models import Category, Customer

# Register your models here.
@admin.register(Category)
class Request_category(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.get_fields()]

@admin.register(Customer)
class Request_customer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']