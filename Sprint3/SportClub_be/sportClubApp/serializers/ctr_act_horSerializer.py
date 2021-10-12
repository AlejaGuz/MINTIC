from sportClubApp.models.actividad import Actividad
from sportClubApp.models.ctr_act_hor import CtrActHor
from sportClubApp.models.horario import Horario
from rest_framework import serializers
from sportClubApp.models.usuario import Usuario
from sportClubApp.serializers.actividadSerializer import ActividadSerializer
from sportClubApp.serializers.horarioSerializer import HorarioSerializer
from sportClubApp.serializers.usuarioSerializer import UsuarioSerializer


class CtrActHorSerializer(serializers.ModelSerializer):

    actividad = ActividadSerializer()
    centro = UsuarioSerializer()
    horario = HorarioSerializer()

    class Meta:
        model = CtrActHor
        fields = ['id_clase', 'centro','actividad','horario']

    def create(self, validated_data):
        vData = validated_data.pop('centro')
        vData = validated_data.pop('actividad')
        vData = validated_data.pop('horario')

        usuarioInstance = Usuario.objects.create(**validated_data)
        actividadInstance = Actividad.objects.create(**validated_data)
        horarioInstance = Horario.objects.create(**validated_data)

        ctrInstance=CtrActHor.objects.create(centro=usuarioInstance,actividad=actividadInstance,horario=horarioInstance, **vData)

        return ctrInstance

    def to_representation(self, obj):
        centro = Usuario.objects.get(id_usuario=obj.centro)
        actividad = Actividad.objects.get(id_actividad=obj.actividad)
        horario = Horario.objects.get(id_horario=obj.horario)
        return {
            'id': obj.id_clase,
            'actividad': {
                'id_actividad': actividad.id_actividad,
                'nombre': actividad.nombre,
                'capacidad': actividad.capacidad
                },
            'centro': {
                'id_usuario': centro.id_usuario,
                'username': centro.username,
                'password': centro.password,
                'email': centro.email,
                'tipo': centro.tipo,
                'plan': centro.plan
                },
            'horario': {
                'id_horario': horario.id_horario,
                'dia': horario.dia,
                'hora': horario.hora
                }

         }