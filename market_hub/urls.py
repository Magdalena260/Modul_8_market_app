"""
URL configuration for market_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import ManufacturerList, ManufacturerDetail, ProductList, ProductDetail, ManufacturerUserList, ManufacturerUserDetail, ManufacturerProductListCreate

urlpatterns = [
    path('manufacturers/', ManufacturerList.as_view(), name='manufacturer-list'),
    path('manufacturers/<int:pk>/', ManufacturerDetail.as_view(), name='manufacturer-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('manufacturer-users/', ManufacturerUserList.as_view(), name='manufactureruser-list'),
    path('manufacturer-users/<int:pk>/', ManufacturerUserDetail.as_view(), name='manufactureruser-detail'),
    path('manufacturers/<int:manufacturer_id>/products/', ManufacturerProductListCreate.as_view(), name='manufacturer-product-list-create'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/market/', include('market_app.api.urls')),
    path ('api/auth/', include('user_auth_app.api.urls')),
    path('api-auth', include ('rest_framework.urls'))
]
