from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def index (request):
    return render(request, 'Blog/index.html')

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'Blog/blogpost.html',{'post':post})


