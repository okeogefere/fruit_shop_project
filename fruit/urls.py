from django.urls import path
from . import views

urlpatterns = [
    #home url
    path('', views.home, name='home'),

    #cart url
    path('cart/', views.cart, name='cart'),

    #shop url
    path('shop/', views.shop, name='shop'),

    #contact url
    path('contact/', views.contact, name='contact'),

    #product details url
    path('product-details/<pid>/', views.product_details, name='product-details'),


    #add to cart url
    path('add-to-cart/', views.add_to_cart, name="add-to-cart"),


    #delete item from cart url
    path('delete-item-from-cart/', views.delete_item_from_cart, name="delete-item-from-cart"),
]
