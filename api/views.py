from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def bili_info():
    with open("../resource/info.json", "r", encoding="utf-8") as f:
        return HttpResponse(f.read())
