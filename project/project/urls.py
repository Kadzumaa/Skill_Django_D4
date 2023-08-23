"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from forms.views import (ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete)

urlpatterns = [
    # path('', admin.site.urls),
    path('news/search/', ProductsList.as_view(), name='product_search'),
    path('news/create/', ProductCreate.as_view(), name='product_create'),
    path('news/<int:pk>/delete', ProductDelete.as_view(), name='product_delete'),
    path('articles/<int:pk>/edit/', ProductUpdate.as_view(), name='product_update'),
    path('articles/<int:pk>/delete', ProductDelete.as_view(), name='product_delete')
]