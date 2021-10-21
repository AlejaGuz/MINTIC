from rest_framework import serializers
from sportClubApp.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'email', 'tipo','plan']