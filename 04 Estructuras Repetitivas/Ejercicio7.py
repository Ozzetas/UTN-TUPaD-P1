'''Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.'''

numero = int(input("Ingrese un numero entero positivo: "))
sumatoria = 0
while numero < 0:
    numero = int(input("ERROR, ha ingresado un numero negativo, ingrese un numero positivo: "))

for i in range(1, numero):
    sumatoria += i
    print(sumatoria)