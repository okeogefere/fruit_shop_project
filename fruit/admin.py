from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'image', 'price', 'featured', 'product_status']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'category_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'price', 'paid_status', 'order_date', 'product_status'] 

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = [ 'order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'product', 'review', 'rating']


admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(CartOrder, CartOrderAdmin)

admin.site.register(CartOrderItems, CartOrderItemsAdmin)

admin.site.register(ProductReview, ProductReviewAdmin)
