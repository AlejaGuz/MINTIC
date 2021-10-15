from sportClubApp.models.actividad import Actividad
from sportClubApp.models.ctr_act_hor import CtrActHor
from sportClubApp.models.horario import Horario
from rest_framework import serializers
from sportClubApp.models.usuario import Usuario
from sportClubApp.serializers.actividadSerializer import ActividadSerializer
from sportClubApp.serializers.horarioSerializer import HorarioSerializer
from sportClubApp.serializers.usuarioSerializer import UsuarioSerializer


class CtrActHorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CtrActHor
        fields = ['id_clase', 'centro','actividad','horario']