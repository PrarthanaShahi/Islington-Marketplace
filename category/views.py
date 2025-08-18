from django.shortcuts import render, get_object_or_404
from products.models import Product
from .models import Category

def category_products(request, category_slug):
    """
    View to display a list of products for a specific category.
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, status=True)
    all_categories = Category.objects.all()

    context = {
        'category': category,
        'products': products,
        'all_categories': all_categories,
    }
    
    return render(request, 'products/products.html', context)
