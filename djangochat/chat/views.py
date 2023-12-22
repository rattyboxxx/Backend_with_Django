from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from chat.models import Room, Message


# Create your views here.
def home(request: HttpRequest):
    return render(request, "home.html")


def room(request: HttpRequest, room: str):
    try:
        username = request.GET.get("username").strip().lower()
        room_details = Room.objects.get(name=room.strip())

        return render(
            request,
            "room.html",
            {"username": username, "room": room.strip(), "room_details": room_details},
        )
    except:
        return render(request, "room.html")


def checkview(request: HttpRequest):
    room = request.POST["room_name"].strip()
    username = request.POST["username"].strip().lower()

    if room and username:
        if Room.objects.filter(name=room).exists():
            return redirect("/" + room + "/?username=" + username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect("/" + room + "/?username=" + username)


def send(request: HttpRequest):
    message = request.POST["message"]
    username = request.POST["username"].strip().lower()
    room_id = request.POST["room_id"]

    # print(dict(request.POST))

    if message:
        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()

        return HttpResponse("Ok")
    else:
        return HttpResponse("No")


def getMessages(request: HttpRequest, room: str):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
