from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'landing/index.html')

def team(request):
    return render(request, 'landing/team.html')

def tc(request):
    return render(request, 'landing/terms-and-conditions.html')

def services(request):
    return render(request, 'landing/services.html')