from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='fotos'
urlpatterns = [
    path('a/', views.a,name='a'), 
    #vista principal
    path('photos/', views.home,name='home'), 
    path('catalog/', views.catalog,name='catalog'), 
    path('facturacion/', views.check,name='check'),
    
    path('agregar/<int:producto_id>/', views.agregar_producto,name='Add'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto,name='Del'),
    path('restar/<int:producto_id>/', views.restar_producto,name='Sub'),
    path('limpiar/', views.limpiar_carrito,name='CLS'),
    path('enviar_carrito/', views.enviar_carrito, name='enviar_carrito'),
    
    path('detalles/<int:prod_id>/',views.prod_detalles, name='prod_detalles'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
