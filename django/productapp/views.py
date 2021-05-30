from productapp.forms import ProductForm
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from productapp.models import Categories, Product
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib import auth

# Create your views here.
def index(request):
    return HttpResponse('Index page')

# def products(request):
#    products = Product.objects.all()
#    return render(request, 'products/products.html', {'products': products})

class CategoryList(ListView):
    model = Categories
    template_name = 'category/category.html'
    context_object_name = 'categories'
 #   extra_context = { Product.objects.filter(): Categories }

class CategoryCreate(CreateView):
    model = Categories
    template_name = 'category/category_create.html'
    fields = ['category_name', 'category_added_date', 'descriptions']
    success_url = reverse_lazy('products:product_list')

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'productdetails'

class ProductCreate(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    fields = ['product_name', 'photo', 'created_date', 'category']
    # form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    # form_class = ProductForm
    fields = ['product_name', 'photo', 'created_date', 'category']
    success_url = reverse_lazy('products:product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:product_list')


def login(request):
    if request.user.is_authenticated():
        return redirect('base')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('base')
        
        else:
            print('Wrong username or password')

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'registration/logout.html')

        

