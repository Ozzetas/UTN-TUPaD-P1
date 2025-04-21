'''Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.'''

numero = int(input("Ingrese un numero entero: "))
numero_abs = abs(numero)
cantidad_digitos = 0

while numero_abs > 0:
    cantidad_digitos += 1
    numero_abs = numero_abs // 10
print(f"El numero tiene: {cantidad_digitos} digitos.")