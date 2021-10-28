from django.conf import settings
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from sportClubApp.serializers import CtrActHorSerializer


class CtrActHorCreateView(views.APIView):
  
  permission_classes = (IsAuthenticated,)

  def post(self, request, *args, **kwargs):
    print(request.data) 
    id_user_body = int(request.data.pop("id_user"))
     
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)

    if valid_data['user_id'] != id_user_body:
      stringResponse = {'detail':'Unauthorized Request'}
      return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
 
    serializer = CtrActHorSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    stringResponse = {'detail':'Excelente'}

    return Response(stringResponse,status=status.HTTP_201_CREATED)