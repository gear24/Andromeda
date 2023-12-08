from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    descripcion = models.CharField(max_length=64, null=True)
    

    def __str__(self):
        return f'{self.nombre}'

@receiver(pre_delete, sender=Producto)
def delete_image(sender, instance, **kwargs):
    # Eliminar la imagen del sistema de archivos cuando se elimina el objeto
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)



class Compra(models.Model):
    usuario = models.CharField(max_length=50, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    lugar_envio = models.CharField(max_length=100, null=True)
    fecha_entrega = models.DateField(null=True)
    contacto_1 = models.CharField(max_length=50, null=True)
    contacto_2 = models.CharField(max_length=50, null=True)
    departamento =models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return f'Id de compra {self.id}'

class DetallesCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(null=True)
    usuario = models.CharField(max_length=50, null=True)

    def save(self, *args, **kwargs):
        # Establece el campo "fecha" en "DetallesCompra" como la fecha de la compra asociada
        self.fecha = self.compra.fecha
        # Establece el campo "usuario" en "DetallesCompra" como el usuario de la compra asociada
        self.usuario = self.compra.usuario
        super(DetallesCompra, self).save(*args, **kwargs)

    def __str__(self):
        return f'Detalles de Compra - Producto: {self.producto}, Cantidad: {self.cantidad}, Usuario: {self.usuario}'

