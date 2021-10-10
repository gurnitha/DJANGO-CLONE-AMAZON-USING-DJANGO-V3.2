# config/urls.py

# Django modules
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.main.urls', namespace='main')),
    path('admin/', admin.site.urls),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
