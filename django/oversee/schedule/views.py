from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
	#return render(request, "schedule/home.html")
	return redirect('home')
 # return HttpResponse("Hello, world. You can make a schedule here")

def home(request):
	if(request.GET.get('mybtn')):
		return redirect('dashboard')
	return render(request, "schedule/home.html")

def dashboard(request):
	return render(request, "schedule/dashboard.html")

def new_channel(request):
	return render(request, "schedule/new_channel.html")

def user_add_availability(request):
	return render(request, "schedule/")



# Testing:






# Create your views here.
