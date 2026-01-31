from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    bikes_title="Lates Bikes"
    return render(request,'index.html',{'heading_bike':bikes_title})
def detail(request):
    return render(request,'detail.html')