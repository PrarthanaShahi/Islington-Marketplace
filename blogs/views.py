from django.shortcuts import render, get_object_or_404
from . models import BlogCategory, Blog

def blogs(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blogs/blogs1.html',{'blogs': all_blogs})

def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blogs/details1.html',{'blog': blog})
