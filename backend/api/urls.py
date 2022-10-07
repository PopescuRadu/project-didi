from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.api_routes, name="api-routes"),

    path('products/', views.api_products, name="api-products"),
    path('products/<slug:slug>/', views.api_products_object, name="api-products-object"),

    path('order-items/', views.api_order_items, name="api-order-items"),

    path('customers/', views.api_customer, name="api-customer"),

    path('shipping-information/', views.api_shipping_information, name="api-shipping-information"),
    path('orders/', views.api_orders, name="api-orders"),
    
]