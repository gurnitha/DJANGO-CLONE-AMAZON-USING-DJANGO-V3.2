# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main.views import (
	adminHome, 
	adminLogin,
	demoPage,)

# from apps.main.admin_views import adminHome

app_name = 'main'

urlpatterns = [
	
	# Admin urls
	path('admin/', adminHome, name='adminHome'), 
	path('admin/login/', adminLogin, name='adminLogin'), 
    path('', demoPage, name='demoPage'),
]
