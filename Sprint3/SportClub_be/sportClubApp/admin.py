from django.contrib import admin
from .models.usuario import Usuario
from .models.actividad import Actividad
from .models.horario import Horario
from .models.ctr_act_hor import CtrActHor
from .models.reserva import Reserva


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Actividad)
admin.site.register(Horario)
admin.site.register(CtrActHor)
admin.site.register(Reserva)
