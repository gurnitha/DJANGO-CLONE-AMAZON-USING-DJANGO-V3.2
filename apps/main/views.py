# apps/main/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def demoPage(request):
	return render(request, 'demo.html')


def adminLogin(request):
	return render(request, 'admin/signin.html')
