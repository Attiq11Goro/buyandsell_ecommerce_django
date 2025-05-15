from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    # price = models.IntegerField()
    price = models.FloatField()  # Original price
    discount_price = models.FloatField(null=True, blank=True)  # Discounted price (optional)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

   
   # we add this code to show plural name and other singular name with corrrect form
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    

    def __str__(self):
        return self.product_name



