from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You can make a schedule here")

# Create your views here.
