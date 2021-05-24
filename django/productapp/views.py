import productapp
from productapp.models import Product
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Index page')

def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

