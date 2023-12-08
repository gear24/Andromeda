from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='Calas'
urlpatterns = [
    path('a/', views.a,name='a'), 
    #vista principal
    path('CreAlas/', views.home,name='home'), 
    path('CreAlas/catalog/', views.catalog,name='catalog'), 
    path('CreAlas/facturacion/', views.check,name='check'),
    
    path('CreAlas/agregar/<int:producto_id>/', views.agregar_producto,name='Add'),
    path('CreAlas/eliminar/<int:producto_id>/', views.eliminar_producto,name='Del'),
    path('CreAlas/restar/<int:producto_id>/', views.restar_producto,name='Sub'),
    path('CreAlas/limpiar/', views.limpiar_carrito,name='CLS'),
    path('CreAlas/enviar_carrito/', views.enviar_carrito, name='enviar_carrito'),
    

    
    path('CreAlas/detalles/<int:prod_id>/',views.prod_detalles, name='prod_detalles'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
