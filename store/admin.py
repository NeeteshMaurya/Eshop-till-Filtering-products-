from django.contrib import admin
from .models.product import Product
from .models.categories import Category

class AdminProduct(admin.ModelAdmin):
    list_display=['name', 'price', 'category']

class CategoryProduct(admin.ModelAdmin):
    list_display=['name',]
# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, CategoryProduct)