from django import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .views import *

from django.shortcuts import get_object_or_404

@api_view(["GET"])
def api_routes(request): #overview of api routes endpoints
    routes = [
    {
        'Endpoint': "/products/",
        'method': "GET",
        'description': 'returns all products',
    },
    {
        'Endpoint': "/products/<slug:slug>/",
        'method': "GET",
        'description': 'returns a single product object',
    },
    {
        'Endpoint': "/customer/",
        'methods' : "GET, POST",
        'description': "returns & retrieves customers",
    },
    {
        'Endpoint': "/customer/shipping-information",
        'methods' : "POST",
        'description': "retrieve the shipping information of the order based on customers device",
    },
    {
        'Endpoint': "/order-item/",
        'methods' : "GET, POST",
        'description': "return & retrieve products added inside the shopping cart based on customers device",
    },
    {
        'Endpoint': "/order/",
        'methods' : "GET, POST",
        'description': "return & retrieve orders that have performed the checkout operation based on customers device",
    }
    ]
    return Response(routes)

@api_view(["GET"])
def api_products(request): #get all products
    objects = Product.objects.all()
    serializer = ProductSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
def api_products_object(request, slug): #get one product object
    if request.method == "GET":
        object = Product.objects.get(slug=slug)
        serializer = ProductSerializer(object, many=False)
        return Response(serializer.data)

    elif request.method == "POST":
        product = get_object_or_404(Product, slug=slug)
        print(request.data)
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = request.POST['quantity']

@api_view(["GET", "POST"])
def api_order_items(request):
    pass

@api_view(["GET", "POST"])
def api_shipping_information(request):
    pass

@api_view(["GET", "POST"])
def api_orders(request):
    pass

@api_view(["GET", "POST"])
def api_customer(request, device_id):

    if request.method == "GET":
        object = Customer.objects.get(device=device_id)
        serializer = CustomerSerializer(object, many=False)
        return Response(serializer.data)

    elif request.method == "POST":
        serialzer = CustomerSerializer()
        if request.is_valid():
            obj = request.data.get("device")
