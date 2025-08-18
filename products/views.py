from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def products(request, category_slug=None):
    """
    Handles the display of products, either filtered by category or all products.
    Includes pagination to limit the number of products per page.
    """
    products_queryset = Product.objects.filter(status=True)
    
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products_queryset = products_queryset.filter(category=category)
    else:
        products_queryset = products_queryset.order_by('id')

    # Pagination logic, moved outside the conditional statement
    paginator = Paginator(products_queryset, 3)
    page_number = request.GET.get('page')
    paged_products = paginator.get_page(page_number)
    product_count = products_queryset.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, category_slug, product_slug):
    """
    Displays the details of a single product.
    Checks if the product is already in the user's cart.
    """
    try:
        product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    except Product.DoesNotExist:
        raise Http404("Product Not Found")
    
    context = {
        'product': product,
        'in_cart': in_cart,
    }
    return render(request, 'products/details.html', context)


def search(request):
    """
    Performs a search based on a keyword provided in the GET request.
    Searches for the keyword in product names or descriptions.
    """
    products_queryset = Product.objects.none()
    
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword', '').strip()
        
        if keyword:
            products_queryset = Product.objects.order_by('-created_at').filter(
                Q(description__icontains=keyword) | Q(name__icontains=keyword)
            )

    # Add pagination logic to the search results
    paginator = Paginator(products_queryset, 3)
    page_number = request.GET.get('page')
    paged_products = paginator.get_page(page_number)
    product_count = products_queryset.count()
            
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'products/products.html', context)
