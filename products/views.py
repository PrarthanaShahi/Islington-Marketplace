from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . models import Category, Product
# from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def products(request, category_slug=None):
    categories = None
    products = None
    # all_products = Product.objects.all()
    # return render(request, 'products/products.html', {'products': all_products})
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category=categories, status=True)
        Paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products - paginator.get_page(page)
        product_count = len(paged_products)

    else:
        products = Product.objects.all().filter(status=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = len(paged_products)

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'products/products.html', context)

# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'products/details1.html', {'product': product})

def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()

    except Product.DoesNotExist:
        raise Http404("Product Not Found")
    
    context={
        'product': product,
        in_cart: in_cart
    }
    return render(request, 'products/details.html',context)