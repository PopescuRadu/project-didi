from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'base/home.html')

def contact(request):
  return render(request, 'base/contact.html')

def about(request):
  return render(request, 'base/about.html')

def policy_privacy():
  pass

def policy_shipping():
  pass

def policy_terms():
  pass

def policy_refund():
  pass