from django.contrib import admin
from . models import BlogCategory, Blog
from django.utils.html import format_html 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    # FIX 1: Corrected typo from 'execlude' to 'exclude'
    exclude = ('created_at',)
    
    # FIX 2: Added 'image_preview' to the list_display tuple
    list_display = ('title', 'category', 'description', 'status', 'image_preview') 
    
    search_fields = ("title", "description")
    list_filter = ("category", "status")
    readonly_fields = ('image_preview',)

    # Custom method to display image preview in the admin list and detail view
    def image_preview(self, obj):
        if obj.blog_image: # Check if an image is associated with the blog object
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit:cover; border-radius: 5px;" />',
                obj.blog_image.url
            )
        return "No image"
    # Sets the column header for the image_preview in the admin list
    image_preview.short_description = 'Image'

admin.site.register(BlogCategory, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)