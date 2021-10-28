"""sportClubProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from sportClubApp import views
from sportClubApp.views.horarioDetailView import HorarioDetailView



urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UsuarioCreateView.as_view()),
    path('user/<int:pk>/', views.UsuarioDetailView.as_view()),
    path('actividad/', views.ActividadCreateView.as_view()),
    path('horario/', views.HorarioCreateView.as_view()),
    path('fusion/', views.CtrActHorCreateView.as_view()),
    path('reserva/', views.ReservaCreateView.as_view()),
    path('fusionread/<int:pk>/', views.CtrActHorDetailView.as_view()),
    path('fusionupdate/<int:pk>/', views.CtrActHorUpdateView.as_view()),
    path('fusiondelete/<int:pk>/', views.CtrActHorDeleteView.as_view()),
    path('horariodelete/<int:pk>/', views.HorarioDeleteView.as_view()),
    path('horariodetail/<int:pk>/',views.HorarioDetailView.as_view()),
    path('horarioupdate/<int:pk>/',views.HorarioUpdateView.as_view()),
    path('fusionreadall/',views.ListaCtrActHorView.as_view()),
    path('actividadread/<int:pk>/',views.ActividadDetailView.as_view()),
    path('horarioreadall/',views.ListaHorarioView.as_view()),
]
