'''Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.'''

import random

numero_aleatorio = random.randint(0, 9)
numero = int(input("Adivine el numero generado entre el 0 y el 9: "))
contador = 1
while numero != numero_aleatorio:
    numero = int(input("Incorrecto, intente nuevamente adivinar el numero generado entre el 0 y el 9: "))
    contador += 1
print(f"CORRECTO!: El numero es: {numero_aleatorio}")
print(f"Fueron necesarios {contador} intentos para adivinar el numero")