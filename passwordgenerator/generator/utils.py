import random
import string

def generar_contraseña(longitud, caracteres):
    """
    Genera una contraseña aleatoria basada en la longitud 
    y los tipos de caracteres seleccionados.

    longitud: La longitud de la contraseña a generar.
    caracteres: Lista de tipos de caracteres seleccionados 
    ('letras', 'numeros', 'simbolos').

    return: La contraseña generada.
    """
    tipos_caracteres = ''
    if 'letras' in caracteres:
        tipos_caracteres += string.ascii_letters
    if 'numeros' in caracteres:
        tipos_caracteres += string.digits
    if 'simbolos' in caracteres:
        tipos_caracteres += string.punctuation

    contraseña = ''.join(random.choice(tipos_caracteres) 
                         for _ in range(longitud))
    return contraseña