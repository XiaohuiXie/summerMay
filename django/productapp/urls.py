
from productapp import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('index/', views.index, name='index'),
    path('product/', views.products, name='products'),

]

urlpatterns += staticfiles_urlpatterns()