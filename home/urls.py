from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    #vista principal
    path('', views.home,name='home'),
    #vista de registro
    
]
