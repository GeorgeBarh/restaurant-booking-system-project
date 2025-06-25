from django.shortcuts import render
from django.http import HttpResponse


def my_reservation(request):
    return HttpResponse("Hello, reservation!")