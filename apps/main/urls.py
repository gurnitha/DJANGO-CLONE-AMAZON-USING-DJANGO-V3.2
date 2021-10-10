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
	CategoriesListView)

# from apps.main.admin_views import adminHome

app_name = 'main'

urlpatterns = [
	
	# Admin urls
	path('admin/', adminHome, name='adminHome'), 
	path('admin/login/', adminLogin, name='adminLogin'),  
	path('admin/login_process/', adminLoginProcess, name='adminLoginProcess'), 
	path('admin/logout_process/', adminLogoutProcess, name='adminLogoutProcess'),
	path('admin/categories', CategoriesListView.as_view(), name='CategoriesListView'), 
    path('', demoPage, name='demoPage'),
]
