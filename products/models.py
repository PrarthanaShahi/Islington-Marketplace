from django.db import models
from django.utils import timezone
# from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    # Add the status field to the Category model
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField(default=1)
    # Add the status field to the Product model
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    product_image = models.ImageField(upload_to='photos/products', blank=True)

    # def get_url(self):
    #     return reverse('product_detail', args=[self.category.slug, self.slug])
    def __str__(self):
        return self.name