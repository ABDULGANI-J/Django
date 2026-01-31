from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    bikes_title="Lates Bikes"
    posts = [
        {'id':1, 'title':'post 1','content':'content of post 1'},
        {'id':2, 'title':'post 2','content':'content of post 2'},
        {'id':3, 'title':'post 3','content':'content of post 3'},
        {'id':4, 'title':'post 4','content':'content of post 4'},
    ]
    return render(request,'index.html',{'heading_bike':bikes_title, 'posts':posts})
def detail(request,post_id):
    return render(request,'detail.html')