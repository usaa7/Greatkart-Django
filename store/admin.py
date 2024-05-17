from django.contrib import admin
from store.models import Product, Product_Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value')


admin.site.register(Product, ProductAdmin) 
admin.site.register(Product_Variation, VariationAdmin) 