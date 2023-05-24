from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
]


#htmx specific url patterns
urlpatterns += [
    path('product_list/<int:cat_id>/', views.ProductListByCategory.as_view(), name='product_list_by_cat'),
    path('product_search/', views.ProductSearchView.as_view(), name='product_search'),    
    
    
    #stats
    
    path('stats/', views.StatsView.as_view(), name='stats'),
]