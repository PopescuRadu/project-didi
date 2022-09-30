from django import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .views import *


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
        'Endpoint': "/products/variants/",
        'method': "GET",
        'description': 'returns all product variants',
    },
    {
        'Endpoint': "/products/variants/<slug:slug>/",
        'method': "GET",
        'description': 'returns a single product variant object',
    },
    {
        'Endpoint': "/products/attributes/",
        'method': "GET",
        'description': 'returns all product attributes objects',
    },
    {
        'Endpoint': "/products/attributes/choices/",
        'method': "GET",
        'description': 'returns all product attributes choices',
    },
    {
        'Endpoint': "/products/images/",
        'method': "GET",
        'description': 'returns all product images',
    },
    {
        'Endpoint': "/products/variants/images/",
        'method': "GET",
        'description': 'returns all product variants images',
    },
    ]
    return Response(routes)

@api_view(["GET"])
def api_products(request): #get all products
    objects = Product.objects.all()
    serializer = ProductSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def api_products_object(request, slug): #get one product object
    object = Product.objects.get(slug=slug)
    serializer = ProductSerializer(object, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def api_products_attributes(request): #get all product attribute objects
    objects = ProductAttribute.objects.all()
    serializer = ProductAttributeSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def api_products_attributes_choices(request): #get all product attribute choices objects
    objects = ProductAttributeChoice.objects.all()
    serializer = ProductAttributeChoiceSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def api_products_variants(request): #get all product variants objects
    objects = ProductVariant.objects.all()
    serializer = ProductVariantSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def api_products_variants_object(request, slug): #get a single product attribute object
    object = Product.objects.get(slug=slug)
    serializer = ProductVariantSerializer(object, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def api_products_images(request): #get all product images
    objects = ProductImage.objects.all()
    serializer = ProductImageSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def api_products_variants_images(request): #get all product images
    objects = ProductVariantImage.objects.all()
    serializer = ProductVariantImageSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def cart_view(request):
    objects = Cart.objects.all()
    serializer = CartSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def cart_post(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("saved cart posted")
    return Response(serializer.data)