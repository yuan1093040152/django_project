from django.shortcuts import render
from django.http import HttpResponse
from . import models


def login(request):
    return render(request,'Login/login.html')