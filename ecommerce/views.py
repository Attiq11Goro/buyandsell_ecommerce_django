from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

def home(request, category_slug=None):
    # products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()
    
    # here we can try to list out categories 
    if category_slug:
        category= get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
       
    else:
        products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    
   
    context = {
        'products': products,
        'categories' :categories,
        'product_count' :  product_count,

    }

    return render(request, "home.html", context)


    


   