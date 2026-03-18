from django.shortcuts import render
from .models import Product
from .models import Order
from django.shortcuts import redirect
def catalog(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})
def orders(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.user.id == 1:
        orders = Order.objects.all
    else:
        orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/orders.html', {'orders': orders})
def product_detail(request, product_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html',{'product': product})
def order_create(request, product_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        Order.objects.create(user=request.user,product=product, delivery_address=request.POST.get('delivery_address'))
        return redirect('orders')
    return render(request, 'shop/order_create.html', {'product':product})
# Create your views here.
