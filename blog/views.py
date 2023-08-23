from django.shortcuts import render, redirect
from .models import Post
from django.template.defaultfilters import slugify


def home(request):
    postListados = Post.objects.all()
    return render(request, "index.html", {"post": postListados})

def verPost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "detail.html", {"post": post})


def registrarPost(request):
    title = request.POST['txtTitle']
    slug = slugify(title)
    content = request.POST['txtContent']

    post = Post.objects.create(
        slug=slug, title=title, content=content)
    return redirect('/')


def edicionPost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "edit.html", {"post": post})


def editarPost(request):
    slug = request.POST['slug']
    title = request.POST['txtTitle']
    content = request.POST['txtContent']

    post = Post.objects.get(slug=slug)
    post.title = title
    post.content = content
    post.save()

    return redirect('/')


def eliminarPost(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()

    return redirect('/')