from django.urls import path

from . import views

urlpatterns = [
  path('catalogue', views.catalogue, name="product-list"),
  path('catalogue/<slug>', views.product, name="product"),
  
  path('cart/', views.cart, name="cart")
  
] 