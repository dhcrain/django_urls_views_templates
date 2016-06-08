from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def bbstat_view(request):
    return HttpResponse("Hello World! stats?")

