from django.shortcuts import render
from .utils import generar_contraseña
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """
    Vista para renderizar la página de inicio.
    """
    return render(request, 'index.html')


def generar(request):
    """
    Vista para generar una contraseña basada 
    en los parámetros proporcionados.
    """
    longitud = int(request.POST.get('longitud'))
    caracteres = request.POST.getlist('caracteres')

    # Si no se selecciona ningún tipo de caracteres, se asume
    #  que se utilizarán letras.
    if not caracteres:
        caracteres = ["letras"]

    contrasena_generada = generar_contraseña(longitud, caracteres)

    context = {
        'contrasena_generada': contrasena_generada,
    }

    return render(request, 'resultado.html', context)