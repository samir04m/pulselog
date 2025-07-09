from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.Index, name='Index'),

    path('login/', CustomLoginView.as_view(), name='Login'),
    path('logout/', views.Logout, name='Logout'),

    # path('init/', views.Init, name='Init'),
]