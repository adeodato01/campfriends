from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages


def landing(request):
    return render(request, "login/index.html")


def log_reg(request):
    return render(request, "login/login.html")


def registration(request):
    result = User.objects.ValidateTheUser(request.POST)
    if result['status']:
        request.session['user_id'] = result['user_id']
        return redirect('/campfriends/travels')
    else:
        print(result['errors'])
        for error in result['errors']:
            messages.error(request, error)
        return redirect('/login')


def login(request):
    result = User.objects.ValidateLogin(request.POST)
    if result['status']:
        request.session['user_id'] = result['user_id']
        return redirect('/campfriends/travels')
    else:
        print(result['errors'])
        for error in result['errors']:
            messages.error(request, error)
        return redirect('/login')

