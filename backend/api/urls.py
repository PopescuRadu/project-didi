from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.api_routes, name="api-routes"),

    path('products/', views.api_products, name="api-products"),
    path('product/<slug:slug>/', views.api_products_object, name="api-products-object"),

    path('products/variants/', views.api_products_variants, name="api-products-variants"),
    path('products/variant/<slug:slug>/', views.api_products_variants_object, name="api-products-variants-object"),
    
    path('products/attributes/', views.api_products_attributes, name="api-products-attributes"),
    path('products/attributes/choices/', views.api_products_attributes_choices, name="api-products-attributes-choices"),

    path('products/images/', views.api_products_images, name="api-products-images"),
    path('products/variants/images/', views.api_products_variants_images, name="api-products-variants-images"),
]