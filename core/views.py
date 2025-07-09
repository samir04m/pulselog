from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.db import transaction


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

def Logout(request):
    logout(request)
    return redirect('main:Login')

@login_required
def Index(request):
    return HttpResponse('Pureba')