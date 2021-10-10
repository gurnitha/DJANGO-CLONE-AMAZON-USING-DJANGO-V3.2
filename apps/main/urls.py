# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main.views import demoPage

app_name = 'main'

urlpatterns = [
    path('', demoPage, name='demoPage'),
]
