# config/admin_views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Locals
from apps.main.models import Categories

# Create your views here.

# Views method:adminHome
@login_required(login_url="/admin/")
def adminHome(request):
	return render(request, 'template_admin/index.html')


# Class views:CategoriesListView
class CategoriesListView(ListView):
	model=Categories
	template_name="template_admin/category_list.html"