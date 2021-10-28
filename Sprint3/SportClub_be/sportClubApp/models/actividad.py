from django.db import models


class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 50, unique=True)
    capacidad = models.IntegerField(default=0)