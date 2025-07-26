from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
from blogs.models import Blog, BlogCategory

def home(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()[:3]

    return render(request, 'home/home1.html', {
        'products': products,
        'blogs' : blogs
        })



