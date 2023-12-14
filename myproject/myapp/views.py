from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Feature
from django.http import HttpRequest
from django.contrib import auth


# Create your views here.
def index(request: HttpRequest):
    features = Feature.objects.all
    return render(request, "index.html", {"features": features})


def counter(request: HttpRequest):
    posts = [1, 2, 3, 4, 5, "tim", "tom", "john"]
    return render(request, "counter.html", {"posts": posts})


def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credential invalid")
            return redirect("login")
    else:
        return render(request, "login.html")


def register(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect("register")
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Password not the same")
            return redirect("register")
    else:
        return render(request, "register.html")


def logout(request: HttpRequest):
    auth.logout(request)
    return redirect("/")


def post(request: HttpRequest, pk: str):
    return render(request, "post.html", {"pk": pk})
