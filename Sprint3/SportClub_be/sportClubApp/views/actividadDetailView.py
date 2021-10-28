from django.conf import settings
from rest_framework import generics,status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from sportClubApp.models.actividad import Actividad
from sportClubApp.serializers.actividadSerializer import ActividadSerializer

class ActividadDetailView(generics.RetrieveAPIView):
  
  permission_classes = (IsAuthenticated,)
  
  def get(self, request, *args, **kwargs):

    id_user_body = int(request.data.pop("id_user"))    
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)

    if valid_data['user_id'] != id_user_body:
      stringResponse = {'detail':'Unauthorized Request'}
      return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    actividad= Actividad.objects.filter(id_actividad=kwargs['pk']).first()
    serializer = ActividadSerializer(actividad)
    return Response(serializer.data)
    