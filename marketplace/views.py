from django.shortcuts import render
from products.models import Category, Product
# from blogs.models import Blog
# from pages.models import Page

def home(request):
    # Retrieve all products that are active (status=True)
    products = Product.objects.all().filter(status=True) 

    # # Retrieve all blogs (no status filter applied here)
    # blogs = Blog.objects.all()[:3] 
    
    # # Retrieve all pages (no status filter applied here)
    # pages = Page.objects.all() 
    
    # Retrieve all categories that are active (status=True)
    categories = Category.objects.all().filter(status=True) 

    context = {
        'products': products,
        # 'blogs': blogs,
        # 'pages': pages,
        'categories': categories
    }

    return render(request, 'home/home.html', context)