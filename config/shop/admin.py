from django.contrib import admin
from .models import Product
from .models import Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','product')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','is_available')
# Register your models here.
