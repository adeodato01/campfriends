from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def info (request):
	if "user_id" not in request.session:
		return redirect('/login')
	user=User.objects.get(id=request.session['user_id'])
	request.session['first_name']=user.first_name
	return render(request, 'campfriends/info.html')

def add_info (request):
	if "user_id" not in request.session:
		return redirect('/login')
	user=User.objects.get(id=request.session['user_id'])
	request.session['first_name']=user.first_name
	return render(request, 'campfriends/add_info.html')

def process_info (request):
	return redirect('/info')

def travels (request):
	return render(request, 'campfriends/travels.html')

def logout (request):
	request.session.clear()
	return redirect('/')