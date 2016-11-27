from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
	#return render(request, "schedule/home.html")
	return redirect('home')
 # return HttpResponse("Hello, world. You can make a schedule here")

def home(request):
	return render(request, "schedule/home.html")

def dashboard(request):
	return render(request, "schedule/dashboard.html")



# Create your views here.
