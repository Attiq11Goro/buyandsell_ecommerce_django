from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category

# View to render the store page




def store(request, category_slug=None):
    categories = Category.objects.all()



    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    product_count = products.count()


     # Get price filter from query params like ?price=100-200
    price_filter = request.GET.get('price')
    if price_filter:
        try:
            min_price, max_price = map(int, price_filter.split('-'))
            products = products.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            # Invalid filter format, fallback to all
            pass
    price_ranges = [
                 {'label': '$0 - $100', 'query': '0-100'},
                {'label': '$100 - $200', 'query': '100-200'},
                {'label': '$200 - $500', 'query': '200-500'},
                {'label': '$500 - $1000', 'query': '500-1000'},
                {'label': '$2000 - $5000', 'query': '2000-5000'},
                {'label': '$100000 - $500000', 'query': '100000-500000'},
                {'label': '$1000000 - $5000000', 'query': '1000000-5000000'},
]

    context = {
        'products': products,
        'product_count': product_count,
        'categories': categories,
        'price_ranges' : price_ranges,

    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug= product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
    }



    return render(request, 'store/product_detail.html', context)





# def store(request, category_slug=None):


#     categories = None
#     products = None

#     if category_slug !=None:
#         categories = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(category=categories, is_available=True)
#         product_count = products.count()
#     else:
#        products = Product.objects.all().filter(is_available=True)
#     product_count = products.count()

#     context = {
#         'products': products,
#         'product_count ' : product_count,
#     }

#     return render(request, 'store/store.html', context)




