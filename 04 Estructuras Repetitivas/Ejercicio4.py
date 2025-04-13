'''Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.'''

numero = 1
sumatoria = 0
condicion = True
while condicion == True:
    numero = int(input("Ingrese un numero para sumarlo: "))
    sumatoria += numero
    print(f"La sumatoia es: {sumatoria}")
    if numero == 0:
        condicion = False