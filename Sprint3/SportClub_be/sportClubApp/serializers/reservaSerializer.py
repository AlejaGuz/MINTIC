from sportClubApp.models.ctr_act_hor import CtrActHor
from sportClubApp.models.reserva import Reserva
from rest_framework import serializers
from sportClubApp.models.usuario import Usuario
from sportClubApp.serializers import usuarioSerializer
from sportClubApp.serializers.usuarioSerializer import UsuarioSerializer
from sportClubApp.serializers.ctr_act_horSerializer import CtrActHorSerializer



class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'usuario','clase','fecha','valor','estado']
