from django.contrib import admin
from .models import Producto, DetallesCompra,Compra


# Register your models here.

class DetallesComprasAdmin(admin.ModelAdmin):
    list_filter=('compra','producto', 'fecha', 'cantidad','usuario',)
    list_display=('compra','producto', 'fecha', 'cantidad','usuario',)
    #list_filter=('compra','producto', 'fecha', 'cantidad',)
    #list_display=('compra','producto', 'fecha', 'cantidad',)


class CompraAdmin(admin.ModelAdmin):
    list_filter=('usuario','fecha', 'id',)
    list_display=('usuario','fecha', 'id',)



admin.site.register(Producto)
admin.site.register(DetallesCompra,DetallesComprasAdmin)
admin.site.register(Compra,CompraAdmin)
