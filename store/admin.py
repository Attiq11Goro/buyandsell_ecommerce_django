from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 
                    'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

# we add this code to show the variation in the admin panel
class VariationAdmin(admin.ModelAdmin):
      list_display = ('product', 'variation_category', 'variation_value', 'is_active')
      
      # so now we want to add some code so if we want to active or deactive the item directly from this admin site 
      list_editable = ('is_active',)
      # so now we also add , after the is active because it is tuple so we add this comma

      # we also want to filter it and it this filter in the admin panel on the right side
      list_filter = ('product', 'variation_category', 'variation_value')
      

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)