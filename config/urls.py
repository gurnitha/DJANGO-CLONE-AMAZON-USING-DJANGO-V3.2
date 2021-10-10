# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('', include('apps.main.urls', namespace='main')),
    path('admin/', admin.site.urls),
]
