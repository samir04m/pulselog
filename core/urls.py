from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.Index, name='Index'),
    path('create_blood_pressure_log', views.create_blood_pressure_log, name='create_blood_pressure_log'),
    path('create_food_log', views.create_food_log, name='create_food_log'),

    path('daily-log/<str:date>/', views.check_daily_log, name='check_daily_log'),

    path('login/', CustomLoginView.as_view(), name='Login'),
    path('logout/', views.Logout, name='Logout'),

    # path('init/', views.Init, name='Init'),
]