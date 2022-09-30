from django.db import models
from django.template.defaultfilters import slugify


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        if self.slug != self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductAttribute(models.Model):
    name = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductAttributeChoice(models.Model):
    name = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    attributes_id = models.ForeignKey(ProductAttribute, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to = "product_images/")
    caption = models.CharField(max_length=500)
    alt_text = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self):
        return self.caption

class ProductVariant(models.Model):
    sku = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    name = models.CharField(max_length=200)
    unit_price = models.FloatField()
    tax_cost = models.FloatField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True)
    attributes_id = models.ManyToManyField(ProductAttribute, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        if self.slug != self.name:
            self.slug = slugify(self.name)
        self.tax_rate = self.unit_price * 0.19
        return super().save(*args, **kwargs)

class ProductVariantImage(models.Model):
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_variant.name




import imp
from django.contrib import admin
from .models import *


class ProductAttributeAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_available']

class ProductAttributeChoiceAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_available']

class ProductImageAdmin(admin.ModelAdmin):
        list_display = ['product', 'caption']

class ProductVariantAdmin(admin.ModelAdmin):
        list_display = ['name', 'unit_price', 'is_available']


admin.site.register(ProductAttributeChoice, ProductAttributeChoiceAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductVariantImage)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product)