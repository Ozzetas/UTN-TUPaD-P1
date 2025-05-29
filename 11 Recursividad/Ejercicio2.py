'''
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''
#Definicion de funciones

def fibonacci_reursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_reursivo(posicion - 1) + fibonacci_reursivo(posicion - 2)
    
#Menu principal

posicion = int(input("Ingrese la posicion para calcular el valor de la serie Fibonacci: "))

print(f"Posicion {posicion} = {fibonacci_reursivo(posicion)}")