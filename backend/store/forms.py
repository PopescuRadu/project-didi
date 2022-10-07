from django import forms
from . import models

class ShippingInformationForm(forms.ModelForm):
  class Meta: 
    model = models.ShippingInformation