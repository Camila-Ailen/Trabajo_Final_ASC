from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Iniciando mi primer clase del proyecto .-.")