# config/admin_views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

# Locals
from apps.main.models import Categories, SubCategories

# Create your views here.

# Views method:adminHome
@login_required(login_url="/admin/")
def adminHome(request):
	return render(request, 'template_admin/index.html')


# ===================Categories===================


# Class views:CategoriesListView
class CategoriesListView(ListView):
	model=Categories
	template_name="template_admin/category_list.html"


# Class views:CategoriesCreateView
class CategoriesCreateView(SuccessMessageMixin,CreateView):
	model=Categories
	success_message="Category added."
	fields="__all__"
	template_name="template_admin/category_create.html"


# Class views:CategoriesUpdateView
class CategoriesUpdateView(SuccessMessageMixin,UpdateView):
	model=Categories
	success_message="Category updated."
	fields="__all__"
	template_name="template_admin/category_update.html"


# ===================Sub Categories===================


# Class views:SubCategoriesListView
class SubCategoriesListView(ListView):
	model=SubCategories
	template_name="template_admin/subcategory_list.html"


# Class views:CategoriesCreateView
class SubCategoriesCreateView(SuccessMessageMixin,CreateView):
	model=SubCategories
	fields="__all__"
	template_name="template_admin/subcategory_create.html"


# Class views:CategoriesUpdateView
class SubCategoriesUpdateView(SuccessMessageMixin,UpdateView):
	model=SubCategories
	fields="__all__"
	template_name="template_admin/subcategory_update.html"