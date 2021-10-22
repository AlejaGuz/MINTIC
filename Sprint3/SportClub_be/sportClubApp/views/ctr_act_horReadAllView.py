from rest_framework.filters import SearchFilter, OrderingFilter
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from sportClubApp.models.ctr_act_hor import CtrActHor
from sportClubApp.serializers.ctr_act_horSerializer import CtrActHorSerializer


class ListaCtrActHorView(generics.ListAPIView):
   
    queryset = CtrActHor.objects. all()
    serializer_class = CtrActHorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['centro', 'actividad', 'horario']
    