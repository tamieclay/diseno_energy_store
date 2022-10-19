# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.urls import path
from .views import OrderListView , OrderDetailView,HomePage
from . import views

app_name = 'apps.home'

urlpatterns = [

    # The home page
    path('', HomePage.as_view(), name="home"),
    path('customer-dash', views.index, name='home'),
    path('admin-dash', OrderListView.as_view(), name="admin"),
    
    path('<pk>/', OrderDetailView.as_view(), name="order-detail"),
    
  
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
