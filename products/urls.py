from django.urls import path
from . import views
from .api_views import ProductListAPI


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
]

urlpatterns += [
    path('api/', ProductListAPI.as_view(), name='product_api'),
]
