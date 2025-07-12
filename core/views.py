from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.db import transaction
from datetime import datetime
from .models import *

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

def Logout(request):
    logout(request)
    return redirect('core:Login')

@login_required
def Index(request):
    now = datetime.now().strftime('%Y-%m-%dT%H:%M')
    return render(request, 'core/home.html', {'now': now})

@login_required
def create_blood_pressure_log(request):
    if request.method == 'POST':
        systolic = request.POST.get('sys')
        diastolic = request.POST.get('dia')
        pulse = request.POST.get('pul')
        annotation = request.POST.get('annotation')
        datetime_str = request.POST.get('datetime')

        if not all([systolic, diastolic, pulse, datetime_str]):
            messages.warning(request, 'Enter all the information')
            return redirect('core:Index')

        try:
            BloodPressureMeasurement.objects.create(
                user=request.user,
                systolic=systolic,
                diastolic=diastolic,
                pulse=pulse,
                annotation=annotation,
                date=getDate(datetime_str)
            )
            messages.success(request, 'Log saved successfully')
        except Exception as ex:
            print(ex)
            messages.error(request, "An error occurred")
    
    return redirect('core:Index')


@login_required
def create_food_log(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        datetime_str = request.POST.get('datetime')

        if not all([description, datetime_str]):
            messages.warning(request, 'Enter all the information')
            return redirect('core:Index')

        try:
            FoodLog.objects.create(
                user=request.user,
                description=description,
                date=getDate(datetime_str)
            )
            messages.success(request, 'Log saved successfully')
        except Exception as ex:
            print(ex)
            messages.error(request, "An error occurred")
    
    return redirect('core:Index')

def getDate(datetime_str):
    try:
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
    except ValueError:
        return timezone.now()