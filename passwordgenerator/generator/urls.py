from django.urls import path
from . import views

app_name = 'generator'

# Rutas para las funcionalidades de la app
urlpatterns = [
    path('', views.index, name='index'),
    path('generar/', views.generar, name='generar'),
]