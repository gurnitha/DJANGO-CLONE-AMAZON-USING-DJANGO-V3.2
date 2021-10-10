# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main.views import (
	demoPage,
	adminLogin,)

app_name = 'main'

urlpatterns = [
	
	# Admin urls
	path('admin/', adminLogin, name='adminLogin'), 
    path('', demoPage, name='demoPage'),
]
