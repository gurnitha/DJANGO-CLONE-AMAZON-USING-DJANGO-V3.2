# apps/main/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def adminHome(request):
	return render(request, 'template_admin/index.html')

def adminLogin(request):
	return render(request, 'template_admin/signin.html')

def demoPage(request):
	return render(request, 'demo.html')

