from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    products = Product.objects.filter(quality='Organic')
    vegetable = Product.objects.filter(category__title='vegetables', quality='Organic').distinct()
    context = {
        'products': products,
        'vegetable': vegetable
        }
    return render(request, 'fruit/index.html', context)



#cart view
def cart(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['quantity']) * float(item['price'])
        return render(request, 'fruit/cart.html', {'cart_data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    else:
        messages.error(request, 'Your Cart is Empty Please add items to cart')
        return redirect('home')
        #return render(request, 'fruit/cart.html', {'cart_data': '', 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})

    




#contact view
def contact(request):
    return render(request, 'fruit/contact.html')



#shop view
def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
        }
    return render(request, 'fruit/shop.html', context)



#product details view
def product_details(request, pid):
    p = Product.objects.get(pid=pid)
    context = {
        'p': p
        }
    return render(request, 'fruit/product-details.html', context)



#add to cart view
def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'quantity': request.GET['quantity'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
        
    }

    if 'cart_data_obj' in request.session:
        if (request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['quantity'] = int(cart_product[str(request.GET['id'])]['quantity'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({'data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})


def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session ['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['quantity']) * float(item['price'])
    
    context = render_to_string('fruit/async/cart-list.html', {'cart_data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({'data': context, 'totalcartitems': len(request.session['cart_data_obj'])})