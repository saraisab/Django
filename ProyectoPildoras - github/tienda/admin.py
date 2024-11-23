from django.contrib import admin
from .models import CategoriaProducto, Producto


# Register your models here.
class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')



#añadimos la clase servicioAdmin
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)