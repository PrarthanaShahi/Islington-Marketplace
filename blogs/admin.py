from django.contrib import admin
from . models import BlogCategory, Blog
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    execlude = ('created_at',)
    list_display = ('title', 'category', 'description','status')

admin.site.register(BlogCategory, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)


