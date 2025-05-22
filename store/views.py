from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q




# View to render the store page




def store(request, category_slug=None):
    categories = Category.objects.all()



    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products, 1) # we set here 6 means we want to show 6 products per page we may change it later
        page = request.GET.get('page') # we get the page number from the url
        paged_products = paginator.get_page(page) 
        product_count = products.count()

    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        # We add pagination concepts here
        paginator = Paginator(products, 6) # we set here 6 means we want to show 6 products per page we may change it later
        page = request.GET.get('page') # we get the page number from the url
        paged_products = paginator.get_page(page) 
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
        'products': paged_products,
        'product_count': product_count,
        'categories': categories,
        'price_ranges' : price_ranges,

    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug= product_slug)

        # we see that added products works or not
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
        "in_cart" : in_cart,
    }



    return render(request, 'store/product_detail.html', context)


# filepath: c:\Users\Panadol\Desktop\drf-project\ecommerce\store\views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def search(request):
    if 'keyword' in request.GET:
       keyword = request.GET['keyword']
       if keyword:
           #here we used Q means we used or function that it may contain the word in descriotion or name
           products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
           product_count = products.count()
    context = {
        'products':products,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html', context)


# def shopdetail(request):
#     return render(request, 'store/product_detail.html')





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




