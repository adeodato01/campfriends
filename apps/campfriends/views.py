from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def info (request):
	return render(request, 'campfriends/info.html')

def add_info (request):
	return render(request, 'campfriends/add_info.html')

def process_info (request):
	return redirect('/info')