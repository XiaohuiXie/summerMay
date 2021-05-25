
from productapp import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('create/', views.ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>', views.ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),

]

# urlpatterns += staticfiles_urlpatterns()