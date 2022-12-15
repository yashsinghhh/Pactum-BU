from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mart.models import Product, Order


def is_seller(user):
    return user.groups.filter(name='seller').exists()
# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required
def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})

@login_required
def cart(request):
    return render(request, 'cart.html')

@login_required
def checkout(request):
    return render(request, 'checkout.html')

@login_required
def order(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order.html', {'orders': orders})

@login_required
def new_product(request):
    if is_seller(request.user):
        return render(request, 'new_product.html')
    else:
        return redirect('products')

@login_required
def create_product(request):
    if request.method == 'POST':
        if not is_seller(request.user):
            return redirect('products')
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image_url = request.POST['image_url']
        user = request.user
        Product.objects.create(name=name, description=description, price=price, image_url=image_url, user=user)
        return render(request, 'new_product.html')
    else:
        return redirect('new_product')