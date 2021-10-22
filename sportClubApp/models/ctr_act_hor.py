from django.db import models
from .usuario import Usuario
from .actividad import Actividad
from .horario import Horario

class CtrActHor(models.Model):

    id_clase = models.AutoField(primary_key=True)
    centro = models.ForeignKey(Usuario, related_name='id_centro', on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, related_name='id_act', on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, related_name='id_hor', on_delete=models.CASCADE)
    