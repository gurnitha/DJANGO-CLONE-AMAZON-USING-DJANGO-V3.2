# config/admin_views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/admin/")
def adminHome(request):
	return render(request, 'template_admin/index.html')