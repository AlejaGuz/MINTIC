from sportClubApp.models.ctr_act_hor import CtrActHor
from sportClubApp.models.reserva import Reserva
from rest_framework import serializers
from sportClubApp.models.usuario import Usuario
from sportClubApp.serializers import usuarioSerializer
from sportClubApp.serializers.usuarioSerializer import UsuarioSerializer
from sportClubApp.serializers.ctr_act_horSerializer import CtrActHorSerializer



class ReservaSerializer(serializers.ModelSerializer):

    clase = CtrActHorSerializer()
    usuario = UsuarioSerializer()

    class Meta:
        model = Reserva
        fields = ['id_reserva', 'usuario','clase','fecha','valor','estado']

    def create(self, validated_data):
        vData = validated_data.pop('usuario')
        vData = validated_data.pop('clase')

        usuarioInstance = Usuario.objects.create(**validated_data)
        claseInstance = CtrActHor.objects.create(**validated_data)

        reservaInstance=Reserva.objects.create(usuario=usuarioInstance,clase=claseInstance, **vData)

        return reservaInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id_usuario=obj.usuario)
        clase = CtrActHor.objects.get(id_clase=obj.clase)
        return {
            'id': obj.id_reserva,
            'usuario': {
                'id_usuario': usuario.id_usuario,
                'username': usuario.username,
                'password': usuario.password,
                'email': usuario.email,
                'tipo': usuario.tipo,
                'plan': usuario.plan
                },
            'clase': {
                'id_clase': clase.id_clase,
                'centro': clase.centro,
                'actividad': clase.actividad,
                'horario' : clase.horario
                }
         }