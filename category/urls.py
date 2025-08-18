from django.urls import path
from . import views

urlpatterns = [
    # This URL pattern is for a single category page, e.g., /category/electronics/
    path('<slug:category_slug>/', views.category_products, name='products_by_category'),
]