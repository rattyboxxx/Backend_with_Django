from django.shortcuts import render
from django.http import HttpRequest
from .models import Post


# Create your views here.
def index(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post(request: HttpRequest, pk: str):
    posts = Post.objects.get(id=pk)
    return render(request, "posts.html", {"posts": posts})
