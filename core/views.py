from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils.timezone import localtime
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
    context = {
        'now': timezone.now(),
        'now_str': datetime.now().strftime('%Y-%m-%dT%H:%M')
    }
    return render(request, 'core/home.html', context)

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

@login_required
def check_daily_log(request, date):
    target_date = datetime.strptime(date, '%Y-%m-%d').date()

    start_datetime = datetime.combine(target_date, datetime.min.time())
    end_datetime = datetime.combine(target_date, datetime.max.time())

    bloodPressureLogs = BloodPressureMeasurement.objects.filter(
        user=request.user,
        date__range=(start_datetime, end_datetime)
    )

    foodLogs = FoodLog.objects.filter(
        user=request.user,
        date__range=(start_datetime, end_datetime)
    )

    # Crear una lista con 24 posiciones (una por cada hora)
    hours = [f"{(h % 12 or 12)}:00 {'AM' if h < 12 else 'PM'}" for h in range(24)]

    # Inicializamos diccionarios para almacenar los logs por hora
    bp_by_hour = {h: [] for h in range(24)}
    food_by_hour = {h: [] for h in range(24)}

    for bp in bloodPressureLogs:
        local_date = localtime(bp.date)
        hour = local_date.hour
        bp_by_hour[hour].append(f"{bp.systolic}, {bp.diastolic}, {bp.pulse}")

    for food in foodLogs:
        local_date = localtime(food.date)
        hour = local_date.hour
        food_by_hour[hour].append(food.description)

    hourly_data = []

    for h in range(24):
        food = food_by_hour.get(h, [])
        bp = bp_by_hour.get(h, [])
        hourly_data.append({
            'hour': hours[h],
            'food': food,
            'bp': bp
        })

    return render(request, 'core/daily_log.html', {
        'hours': hours,
        'hourly_data': hourly_data,
        'date': target_date,
    })

def getDate(datetime_str):
    try:
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
    except ValueError:
        return timezone.now()