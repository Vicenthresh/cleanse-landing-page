from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'landing/index.html')

def team(request):
    return render(request, 'landing/team.html')