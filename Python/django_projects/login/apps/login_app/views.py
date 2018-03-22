from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from models import User
import bcrypt
import re

# Load home page
def index(request):
    context = {
        'Users': User.objects.all(),
    }
    return render(request , "login_app/index.html", context)

def success(request):
    try:
        user = User.objects.get(id=request.session['id'])
        context = {
            'User': user,
        }
        return render(request,"login_app/success.html", context)
    except:
        messages.error(request, "Something went wrong with your login, please try again")
        return redirect("/")

#Create user
def register(request):
    if request.method == "POST":
        #Validation in models.py
        valid, response = User.objects.register_validator(request.POST)
        if valid:
            request.session['id'] = response.id
            request.session['success'] = "registered"
            return redirect('/success')
        else:
            for message in response:
                messages.error(request, message)
            return redirect('/')
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        #Validation in models.py
        valid, response = User.objects.login_validator(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if valid:
            request.session['id'] = response.id
            request.session['success'] = "logged in"
            return redirect("/success")
        else:
            for message in response:
                messages.error(request, message)
            return redirect('/')
    else:
        if  "username" in request.session:
            return redirect('/success')
        else:
            return redirect('/')
         
def logout(request):
    if request.method == "POST":
        del request.session['id']
        del request.session['success']
        return redirect("/")
    else:
        del request.session['id']
        del request.session['success']
        return redirect("/")

