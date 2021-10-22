from django.conf import settings
from rest_framework import generics,status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from sportClubApp.models.horario import Horario
from sportClubApp.serializers import HorarioSerializer

class HorarioDetailView(generics.RetrieveAPIView):
  queryset = Horario.objects.all()
  serializer_class = HorarioSerializer
  permission_classes = (IsAuthenticated,)
  
  def get(self, request, *args, **kwargs):

    id_user_body = request.data.pop("id_user")    
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)

    if valid_data['user_id'] != id_user_body:
      stringResponse = {'detail':'Unauthorized Request'}
      return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    horariod= Horario.objects.filter(id_horario=kwargs['pk']).first()
    serializer = HorarioSerializer(horariod)
    return Response(serializer.data)