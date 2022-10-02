from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def say_hello(request) :
    return HttpResponse("<h1>Hello, Django</h1>")

def home(request) :
    all_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'all_posts': all_posts})

def post_detail(request, pk):
    single_post = Post.objects.get(pk=pk)
    return render(request, 'blog/post-detail.html', {'single_post' : single_post})