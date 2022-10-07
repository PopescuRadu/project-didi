from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Ribbon)
admin.site.register(models.Discount)
admin.site.register(models.ShippingOptions)

admin.site.register(models.ProductProperty)
admin.site.register(models.ProductPropertyValue)

admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.ShippingInformation)

