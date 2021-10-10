# apps/main/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout   
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def adminHome(request):
	return render(request, 'template_admin/index.html')


def adminLogin(request):
	return render(request, 'template_admin/signin.html')


def demoPage(request):
	return render(request, 'demo.html')


def adminLoginProcess(request):
	# Get username and password form the form fields
	username = request.POST.get("username")
	password = request.POST.get("password")

	# Authenticate username and password
	user = authenticate(request=request,username=username,password=password)
	# If user exists, then login
	if user is not None:
		login(request=request,user=user)
		return HttpResponseRedirect(reverse('main:adminHome'))
	# If user not exists
	else:
		messages.error(request, "Invalid login credentials! Try again ...")
		return HttpResponseRedirect(reverse('main:adminLogin'))


def adminLogoutProcess(request):
	logout(request)
	messages.success(request, "Logged out success.")
	return HttpResponseRedirect(reverse("main:adminLogin"))




