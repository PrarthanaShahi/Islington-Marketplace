from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', include('products.urls')),
    path('blogs/', include('blogs.urls')),
    path('pages/', include('pages.urls')),
    # path('login/', views.user_login, name='user_login'),
    # path('register/', views.user_register, name='user_register'),
    # path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('cart/', include('carts.urls')),
    # path('checkout/', views.checkout, name='checkout'),
    # path('place-order/', views.place_order, name='place_order'),
    # path('order-complete/', views.order_complete, name='order_complete'),
    # path('my-orders/', views.my_orders, name='my_orders'),
    # path('edit-profile/', views.edit_profile, name='edit_profile'),
    # path('change-password/', views.change_password, name='change_password'),
    # path('')
]

# This is the crucial part that enables Django's development server to serve uploaded media files.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)