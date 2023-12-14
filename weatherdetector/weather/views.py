from django.shortcuts import render
from django.http import HttpRequest
import urllib.request
import json


# Create your views here.
def index(request: HttpRequest):
    if request.method == "POST":
        city = "_".join(request.POST["city"].lower().split())
        API_key = "0fd98e687497aa668daf203e8de022d9"
        try:
            res = urllib.request.urlopen(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
            ).read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data["sys"]["country"]),
                "coordinate": str(json_data["coord"]["lon"])
                + " "
                + str(json_data["coord"]["lat"]),
                "temp": str(json_data["main"]["temp"]) + "K",
                "pressure": str(json_data["main"]["pressure"]),
                "humidity": str(json_data["main"]["humidity"]),
            }
        except:
            data = {
                "country_code": "Unknown",
                "coordinate": "Unknown",
                "temp": "Unknown",
                "pressure": "Unknown",
                "humidity": "Unknown",
            }
    else:
        city = ""
        data = {
            "country_code": "",
            "coordinate": "",
            "temp": "",
            "pressure": "",
            "humidity": "",
        }

    return render(request, "index.html", {"city": city, "data": data})
