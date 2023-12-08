from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "andro"
urlpatterns = [
    path('a/', views.a,name='a'), 
    #vista principal
    path('andro/', views.home,name='home'), 
    path('catalogo/', views.catalogo,name='catalogo'), 
    path('check/', views.check,name='check'),
    
    path('agrega/<int:producto_id>/', views.agregar_producto,name='Add'),
    path('elimina/<int:producto_id>/', views.eliminar_producto,name='Del'),
    path('resta/<int:producto_id>/', views.restar_producto,name='Sub'),
    path('limpia/', views.limpiar_carrito,name='CLS'),
    path('enviar_carro/', views.enviar_carrito, name='enviar_carrito'),
    
    path('detalle/<int:prod_id>/',views.prod_detalles, name='prod_detalles'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
