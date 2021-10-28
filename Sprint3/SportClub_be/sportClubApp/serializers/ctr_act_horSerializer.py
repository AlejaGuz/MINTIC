from sportClubApp.models.actividad import Actividad
from sportClubApp.models.ctr_act_hor import CtrActHor
from sportClubApp.models.horario import Horario
from rest_framework import serializers
from sportClubApp.models.usuario import Usuario
from sportClubApp.models.actividad import Actividad
from sportClubApp.serializers.actividadSerializer import ActividadSerializer
from sportClubApp.serializers.horarioSerializer import HorarioSerializer
from sportClubApp.serializers.usuarioSerializer import UsuarioSerializer


class CtrActHorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CtrActHor
        fields = ['id_clase', 'centro','actividad','horario']
    
    def to_representation(self, instance):
    
        actividad = Actividad.objects.get(id_actividad=instance.actividad.id_actividad)
        horario = Horario.objects.get(id_horario=instance.horario.id_horario)
        return {
            'id_clase': instance.id_clase,

            'id_centro' : instance.centro.id,
            
            'actividad': {
                'id_actividad' : actividad.id_actividad,
                'nombre' : actividad.nombre,
                'capacidad': actividad.capacidad
            },

            'horario':{
                'id_horario': horario.id_horario,
                'dia': horario.dia,
                'hora': horario.hora
            }
        }