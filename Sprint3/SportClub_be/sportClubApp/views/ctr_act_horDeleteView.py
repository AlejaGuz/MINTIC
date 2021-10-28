from django.conf import settings
from django.views.generic.base import View
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from sportClubApp.models.ctr_act_hor import CtrActHor

class CtrActHorDeleteView(views.APIView):
  
  def delete(self, request, *args, **kwargs):

    permission_classes = (IsAuthenticated,)
    print(request.data)
    
    id_user_body = int(request.data.pop("id_user"))
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)

    if valid_data['user_id'] != id_user_body:
      stringResponse = {'detail':'Unauthorized Request'}
      return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    clase= CtrActHor.objects.filter(id_clase=kwargs['pk']).first()
    clase.delete()
    stringResponse = {'detail':'Registro eliminado'}
    return Response(stringResponse)