from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import Contactform

# Static demo data
# posts = [
#         {'id':1, 'title':'post 1','content':'content of post 1'},
#         {'id':2, 'title':'post 2','content':'content of post 2'},
#         {'id':3, 'title':'post 3','content':'content of post 3'},
#         {'id':4, 'title':'post 4','content':'content of post 4'},
#     ]

def index(request):
    bikes_title="Lates Bikes"

    #get data from post models
    all_posts = Post.objects.all()

    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request,'index.html',{'heading_bike':bikes_title, 'page_obj':page_object})

def detail(request,slug):
    try:
        post=Post.objects.get(slug=slug)
        related_post=Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post does not Exists")
    # post = next((item for item in posts if item['id']==int(post_id)),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post variable is {post}')
    return render(request,'detail.html',{'post': post, 'related_post':related_post})

def contact_view(request):
    if request.method == 'Post':
        form = Contactform(request.POST)
        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'Post Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
        else:
            logger.debug("Form Validation Failure")
    return render(request,'contact.html')