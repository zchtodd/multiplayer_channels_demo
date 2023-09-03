from django.shortcuts import render


def index(request):
    return render(request, "channels_demo/index.html")
