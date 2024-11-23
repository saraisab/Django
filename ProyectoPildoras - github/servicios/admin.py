from django.contrib import admin
from .models import Servicio

# Register your models here.
#vamos a insertar los campos de updated y created de solo lectura
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


#añadimos la clase servicioAdmin
admin.site.register(Servicio, ServicioAdmin)
