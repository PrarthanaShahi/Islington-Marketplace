from django.contrib import admin
from . models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    execlude = ('created_at',)
    list_display = ('name', 'category', 'price', 'stock', 'status')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
