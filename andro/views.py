from datetime import timezone, datetime
import random
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib import messages
from andro.Carrito import Carrito
from andro.models import Producto
from .models import Compra, DetallesCompra
from django.utils import timezone
from django.db.models import Count

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string



def a(request): 
    productos = Producto.objects.all()
    return render(request,"homef.html", {'productos':productos})

def catalogo(request):
    productos = Producto.objects.all()
    carrito = request.session.get('andro', {}).get('carrito', {})  
    categorias = Producto.objects.values('categoria').annotate(total=Count('categoria'))

    for producto in productos:
        producto.en_carrito = False
        for key, value in carrito.items():
            if value['producto_id'] == producto.id:
                producto.en_carrito = True
                producto.cantidad_en_carrito = value['cantidad']
                break

    return render(request, "catalogA.html", {'productos': productos, 'carrito': carrito,'categorias': categorias})

def home(request):
    prod_samples = Producto.objects.all()
    samples = random.sample(list(prod_samples), 3)
    carrito = request.session.get('andro', {}).get('carrito', {})
    data = {'sample': samples, 'carrito': carrito, 'prods':prod_samples}
    return render(request, "homea.html",data)


@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request, app_name='andro')
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
      
    referer = request.META.get('HTTP_REFERER')
    print(referer)

    
    if not referer or referer == request.build_absolute_uri():
        return redirect('catalog') 

    
    return redirect(referer)

@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request, app_name='andro')
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
      
    referer = request.META.get('HTTP_REFERER')
    print(referer)

    
    if not referer or referer == request.build_absolute_uri():
        return redirect('catalog') 

    
    return redirect(referer)

@login_required
def restar_producto(request, producto_id):
    carrito = Carrito(request, app_name='andro')
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
      
    referer = request.META.get('HTTP_REFERER')
    print(referer)

    
    if not referer or referer == request.build_absolute_uri():
        return redirect('catalog') 

    
    return redirect(referer)

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request, app_name='andro')
    carrito.limpiar()
      
    referer = request.META.get('HTTP_REFERER')
    print(referer)

    
    if not referer or referer == request.build_absolute_uri():
        return redirect('catalog') 

    
    return redirect(referer)

@login_required
#para que funcione, debe tener el checkeo de usuario, el decorador de login
def enviar_carrito(request):
    carrito = Carrito(request, app_name='andro')

    if request.method == 'POST':
        # Extraer los datos del formulario del request
        lugar_envio = request.POST.get('address')
        telefono1 = request.POST.get('telefono1')
        telefono2 = request.POST.get('telefono2')
        fecha_entrega = request.POST.get('fecha')
        departamento = request.POST.get('departamento')  
        usuario_actual = request.user
        correo_usuario = usuario_actual.email
        remitente = settings.EMAIL_HOST_USER
        
        # Crear una nueva instancia de Compra y guardarla en la base de datos
        nueva_compra = Compra(usuario=request.user, lugar_envio=lugar_envio,
                              contacto_1=telefono1, contacto_2=telefono2,
                              fecha_entrega=fecha_entrega, fecha=timezone.now(), departamento=departamento)
        messages.success(request, "Su pedido está registrado")
        nueva_compra.save()

        for key, value in request.session.get('andro', {}).get('carrito', {}).items():
            producto_id = value['producto_id']
            cantidad = value['cantidad']

            # Verificar si ya existe un registro para este producto en la compra actual
            detalles_compra_existente = DetallesCompra.objects.filter(compra=nueva_compra, producto_id=producto_id).first()

            if detalles_compra_existente:
                # Si ya existe, actualizar la cantidad en lugar de crear un nuevo registro
                detalles_compra_existente.cantidad += cantidad
                detalles_compra_existente.save()
            else:
                # Si no existe, crear una nueva instancia de DetallesCompra
                detalles_compra = DetallesCompra(compra=nueva_compra, producto_id=producto_id, cantidad=cantidad)
                detalles_compra.save()

        carrito_data = request.session.get('andro', {}).get('carrito', {})
        fecha_actual = datetime.now()
        
        # Renderizar el HTML desde una plantilla
        html_message = render_to_string('Space_Email.html', {'carrito_data': carrito_data, 'fecha':fecha_actual})
        
        # Enviar el correo utilizando send_mail
        subject = 'Solicitud de pedido Andromeda Studios'
        message = 'Texto del correo'
        from_email = remitente
        recipient_list = [correo_usuario]

        try:
            send_mail(subject, message, from_email, recipient_list, html_message=html_message)
        except Exception as e:
            messages.error(request, f"Error al enviar el correo: {e}")
        


        carrito.limpiar()

        # Redirigir al usuario a la página de inicio
        return redirect("andro:home")

    return render(request, "carrito.html")


def prod_detalles(request, prod_id):
    id = get_object_or_404(Producto, pk=prod_id)
    prod_samples = Producto.objects.all()
    samples = random.sample(list(prod_samples), 3)
    
    productos = Producto.objects.all()
    carrito = request.session.get('andro', {}).get('carrito', {}) 
    
    for producto in productos:
        producto.en_carrito = False
        for key, value in carrito.items():
            if value['producto_id'] == producto.id:
                producto.en_carrito = True
                producto.cantidad_en_carrito = value['cantidad']
    
    data = {'prod': id,'sample':samples,'productos': productos,'carrito':carrito}
    print(id)
    return render(request, "detailsA.html",data)

def check(request):
    #id = get_object_or_404(Producto)
    user = request.user
    productos = Producto.objects.all()
    carrito = request.session.get('andro', {}).get('carrito', {}) 
    
    data = { 'user':user, 'productos':productos,'carrito': carrito,} #,'prod': id,}
    return render(request, "checkA.html",data)