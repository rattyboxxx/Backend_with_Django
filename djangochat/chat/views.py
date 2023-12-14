from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from chat.models import Room, Message


# Create your views here.
def home(request: HttpRequest):
    return render(request, "home.html")


def room(request: HttpRequest, room: str):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    return render(
        request,
        "room.html",
        {"username": username, "room_name": room, "room_details": room_details},
    )


def checkview(request: HttpRequest):
    room = request.POST["room_name"]
    username = request.POST["username"]

    if Room.objects.filter(name=room).exists():
        return redirect("/" + room + "/?username=" + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect("/" + room + "/?username=" + username)


def send(request: HttpRequest):
    message = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse("Message sent successfully")
