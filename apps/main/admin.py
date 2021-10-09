# apps/main/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.main.models import Categories, SubCategories

# Register your models here.

admin.site.register(Categories)
admin.site.register(SubCategories) 