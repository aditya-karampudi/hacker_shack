from django.http import HttpResponse
from django.shortcuts import render

def index(request: HttpResponse):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
