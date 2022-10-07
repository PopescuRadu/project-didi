from ast import Or
from django.shortcuts import get_object_or_404, redirect, render

from .models import (
  Product,
  Customer,
  Order,
  OrderItem
)


def product(request, slug):
  obj = get_object_or_404(Product, slug=slug)

  if request.method == "POST":
    product = Product.objects.get(slug=slug)
    try:
      customer = request.user.customer
    except:
      device = request.COOKIES['device']
      customer, created = Customer.objects.get_or_create(device=device)
    
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    orderItem.quantity = request.POST['quantity']
    return redirect('cart')

  return render(request, 'store/product.html', {'obj':obj})

def cart(request):
  try:
    customer = request.user.customer
    
  except:
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)
  
  order, created = Order.objects.get_or_create(customer=customer, complete=False)
  context={"order":order}

  return render(request, 'store/cart.html', context)