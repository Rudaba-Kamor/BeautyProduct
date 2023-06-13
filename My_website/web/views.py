from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
  #  return HttpResponse("Hello world!")
  return render(request,'web/home.html')

def products(request):
  #  return HttpResponse("Hello world!")
  return render(request,'web/products.html')