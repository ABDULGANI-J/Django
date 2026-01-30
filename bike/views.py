from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')
def home(request):
    return HttpResponse("Wellcome")