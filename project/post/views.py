from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    post = Post.objects.all()
    return render(request, 'post/index.html', context={'post': post})


def create(request):
    if request.method == "POST":
        post = Post(request.POST)
        if post.is_valid():
            title = post.cleaned_data['title']
            text = post.cleaned_data['text']
            Post.objects.create(title=title, text=text)
            return redirect('home')
    post = Post()
    return render(request, 'post/create.html', context={'post': post})


def update(request, id):
    try:
        post = Post.objects.get(id=id)
        if request.method == "POST":
            post.title = request.POST.get('title')
            post.text = request.POST.get('text')
            post.save()
            return redirect('home')
        else:
            return render(request, 'post/update.html', context={'post': post})

    except:
        return redirect('create')

def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('home')
    except:
        return redirect('home')

def post(request, id):
    try:
        post = Post.objects.get(id=id)
        return render(request, 'post/post.html', context={'post': post})
    except:
        return redirect('home')
