from django.db import models
from .usuario import Usuario
from .ctr_act_hor import CtrActHor


class Reserva(models.Model):

    id_reserva = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='id_usu', on_delete=models.CASCADE)
    clase = models.ForeignKey(CtrActHor, related_name='id_class', on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.IntegerField(default=0)
    estado = models.IntegerField(default=0)
