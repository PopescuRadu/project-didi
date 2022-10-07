from email.policy import default
from tokenize import blank_re
from django.db import models
from django_countries.fields import CountryField
from colorfield.fields import ColorField
from django.template.defaultfilters import slugify


class ShippingOptions(models.Model):
  description = models.CharField(max_length=400, null=True, blank=True)
  duration = models.CharField(max_length=200, null=True, blank=True)
  price = models.CharField(max_length=200, null=True, blank=True)

class Discount(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True)
  discount_percent = models.DecimalField(decimal_places=4, max_digits=8, null=True, blank=True)
  is_active = models.BooleanField(null=True, blank=True)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.name

class Ribbon(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True)
  color = ColorField(default='#FF0000')

  def __str__(self):
    return self.name

class ProductProperty(models.Model): # reporter
  name = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.name

class ProductPropertyValue(models.Model): #articol
  unit = models.CharField(max_length=50, null=True)
  property_fk = models.ForeignKey(ProductProperty, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.unit

class Product(models.Model):
  name = models.CharField(max_length=250)
  description = models.TextField()
  ribbon_fk = models.ForeignKey(Ribbon, on_delete=models.CASCADE)
  discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
  price = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
  shipping_fk = models.ForeignKey(ShippingOptions, on_delete=models.SET_NULL, null=True)
  property_fk = models.ManyToManyField(ProductProperty, blank=True)
  slug = models.SlugField(null=True, blank=True)
  image = models.ImageField(null=True, blank=True)
  added_on = models.DateTimeField(auto_now_add=True, null=True)
  in_stock = models.BooleanField(default=True)

  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url = ''
    return url

  def save(self, *args, **kwargs): # new
      if not self.slug:
          self.slug = slugify(self.name)
      if self.slug != self.name:
          self.slug = slugify(self.name)
      return super().save(*args, **kwargs)

  def __str__(self):
    return self.name + " - " + self.ribbon_fk.name


class ProductVariant(models.Model):
  product_fk = models.ForeignKey(Product, on_delete=models.CASCADE)
  store_price = models.DecimalField(max_digits=8, decimal_places=4)

class Customer(models.Model):
  first_name = models.CharField(max_length=200, null=True, blank=True)
  last_name = models.CharField(max_length=200, null=True, blank=True)
  email = models.EmailField(max_length=200, null=True, blank=True)
  phone = models.CharField(max_length=200, null=True, blank=True)
  device = models.CharField(max_length=200, null=True, blank=True)
  
class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  ordered_on = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  quantity = models.IntegerField(default=1, null=True, blank=True)
  added_on = models.DateTimeField(auto_now_add=True)

  def total_amount(self):
    return self.quantity * self.product.price

class ShippingInformation(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  address = models.CharField(max_length=200, null=False)
  country = CountryField()
  city = models.CharField(max_length=200, null=False)
  state = models.CharField(max_length=200, null=False)
  zipcode = models.CharField(max_length=200, null=False)
  added_on = models.DateTimeField(auto_now_add=True)