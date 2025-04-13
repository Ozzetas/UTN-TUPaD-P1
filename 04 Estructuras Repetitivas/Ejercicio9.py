'''Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).'''

sumatoria = 0
contador = 1
while contador <= 5:
    numero = int(input("Ingrese un numero entero: "))
    sumatoria += numero
    contador += 1
print(f"La media de los numeros es de {sumatoria/contador}")