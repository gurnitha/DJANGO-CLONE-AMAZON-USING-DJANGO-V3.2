# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main.views import (
	adminLogin,
	demoPage,
	adminLoginProcess,
	adminLogoutProcess)
from apps.main.views_admin import (
	adminHome,
	CategoriesListView,
	CategoriesCreateView,
	CategoriesUpdateView,
	SubCategoriesListView,
	SubCategoriesCreateView,
	SubCategoriesUpdateView)

# from apps.main.admin_views import adminHome

app_name = 'main'

urlpatterns = [
	
	# Admin urls
	path('dashboard/', adminHome, name='adminHome'), 
	path('dashboard/login/', adminLogin, name='adminLogin'),  
	path('dashboard/login_process/', adminLoginProcess, name='adminLoginProcess'), 
	path('dashboard/logout_process/', adminLogoutProcess, name='adminLogoutProcess'),
	
	# Categories
	path('dashboard/categories/', CategoriesListView.as_view(), name='CategoriesListView'), 
	path('dashboard/categories/create/', CategoriesCreateView.as_view(), name='CategoriesCreateView'), 
	path('dashboard/categories/update/<slug:pk>/', CategoriesUpdateView.as_view(), name='CategoriesUpdateView'), 
	
	# Sub Categories
	path('dashboard/subcategories/', SubCategoriesListView.as_view(), name='SubCategoriesListView'), 
	path('dashboard/subcategories/create/', SubCategoriesCreateView.as_view(), name='SubCategoriesCreateView'), 
	path('dashboard/subcategories/update/<slug:pk>/', SubCategoriesUpdateView.as_view(), name='SubCategoriesUpdateView'), 
    
    path('', demoPage, name='demoPage'),
]
