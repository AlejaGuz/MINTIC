from django.conf import settings
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from sportClubApp.models.horario import Horario
from sportClubApp.serializers.horarioSerializer import HorarioSerializer

class HorarioUpdateView(views.APIView):
  def put(self, request, *args, **kwargs):
  
    permission_classes = (IsAuthenticated,)

    id_user_body = request.data.pop("id_user")
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)

    if valid_data['user_id'] != id_user_body:
      stringResponse = {'detail':'Unauthorized Request'}
      return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    horariod= Horario.objects.filter(id_horario=kwargs['pk']).first()
    serializer = HorarioSerializer(horariod, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )