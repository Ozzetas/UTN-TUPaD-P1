'''Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.'''

numero1 = int(input("Ingrese el primer numero distinto de cero: "))
numero2 = int(input("Ingrese el segundo numero distinto de cero: "))
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
print(f"La suma de {numero1} mas {numero2} = {suma}")
print(f"La resta de {numero1} menos {numero2} = {resta}")
print(f"La division entre {numero1} y {numero2} = {division}")
print(f"La multiplicacion entre {numero1} y {numero2} = {multiplicacion}")