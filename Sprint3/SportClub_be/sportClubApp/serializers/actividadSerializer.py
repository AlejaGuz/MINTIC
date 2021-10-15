from sportClubApp.models.actividad import Actividad
from rest_framework import serializers

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['nombre', 'capacidad']