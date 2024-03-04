from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random

# Create your views here.

def login(request):
    return render(request,"societyapp/login.html")

def login_evalute(request):
        memail_var = request.POST["email"]
        mpassword_var = request.POST["password"]
        muid = User.objects.get(email=memail_var ,password=mpassword_var)

        return render(request,"societyapp/index.html")
