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
        return redirect('/travels')
    else:
        print(result['errors'])
        for error in result['errors']:
            messages.error(request, error)
        return redirect('/login')


def login(request):
    result = User.objects.ValidateLogin(request.POST)
    if result['status']:
        request.session['user_id'] = result['user_id']
        return redirect('/travels')
    else:
        print(result['errors'])
        for error in result['errors']:
            messages.error(request, error)
        return redirect('/login')


def test(request):
    return render(request, 'login/test_map_click.html')

def location(request):
    print('\n''\n'"************THIS Map CLICK!**********")
    print(request.POST)
    print("*****************************"'\n''\n')
    return HttpResponse('Okay!')


