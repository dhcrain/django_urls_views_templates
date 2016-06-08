from django.shortcuts import render
from django.http import HttpResponse
from wiring_up.models import BaseballStat
# Create your views here.


def bbstat_view(request):
    return HttpResponse(BaseballStat)

