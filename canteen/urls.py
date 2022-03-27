"""klasseats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from .views import food_menu, food_item_create, food_item_modify, dashboard_view, OrderDetailView, food_item_delete, CreateOrder, add_to_cart

app_name = 'canteen'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', food_menu.as_view(), name='menu'),
    path('create', food_item_create.as_view(),name='create_food'),
    path('add-to-cart/<int:pk>', add_to_cart, name = 'add-to-cart'),
    path('modify/<int:pk>/', food_item_modify.as_view(), name='modify_food'),
    path('delete/<int:pk>/', food_item_delete.as_view(), name='delete_food'),    
    path('dashboard/', views.dashboard_view, name = 'dashboard'),
    path('order-detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),   
     
]
