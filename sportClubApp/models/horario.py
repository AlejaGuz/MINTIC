from django.db import models


class Horario(models.Model):

    id_horario = models.AutoField(primary_key=True)
    dia = models.CharField('Dia', max_length = 50)
    hora = models.IntegerField(default=0)