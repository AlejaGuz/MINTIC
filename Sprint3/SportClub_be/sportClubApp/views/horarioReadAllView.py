from rest_framework.filters import SearchFilter, OrderingFilter
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from sportClubApp.models.horario import Horario
from sportClubApp.serializers.horarioSerializer import HorarioSerializer


class ListaHorarioView(generics.ListAPIView):
   
    queryset = Horario.objects. all()
    serializer_class = HorarioSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id_horario','nombre', 'capacidad']