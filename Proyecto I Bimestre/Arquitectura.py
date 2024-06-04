
#                       PROYECTO ARQUITECTURA - METODOS NUMERICOS

# Paquetes necesarios
from scipy.optimize import newton
import math

# Funcion que calcula W
def w(x1, x2, h):
    root = newton(func = lambda w : (h*w) / (x2**2 - w**2)**0.5 + (h*w) / (x1**2 - w**2)**0.5 - w, x0 = 2.5)
    return root

# INICIO DEL PROGRAMA

# Control de entrada de enteros usando excepciones
while True:
    x1 = input("Ingrese el valor de la longitud de la escalera 1 en metros (m): ")
    x2 = input("Ingrese el valor de la longitud de la escalera 2 en metros (m): ")
    h = input("Ingrese la altura en metros desde el suelo hacia la intersección entre las escaleras: ")
    
    try:
        x1 = float(x1)
        x2 = float(x2)
        h = float(h)
        
    except:
        print("Ingrese números por favor")
        
    else:
        break

root = w(x1, x2, h)
print(f"El valor en metros de la distancia o ancho del pasillo para las escaleras y su altura es: {root}")