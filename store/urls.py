
from django.urls import path
from . import views




urlpatterns = [
   path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
   path('category/<slug:category_slug>/', views.store, name='products_by_category'),
   path('', views.store, name='store'),
   path('search/', views.search, name='search'), # added search url

]

    
