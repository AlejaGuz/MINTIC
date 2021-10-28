from sportClubApp.models.horario import Horario
from rest_framework import serializers

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id_horario','dia', 'hora']